from collections import defaultdict
from itertools import combinations

def indexing(friends):
    fri = defaultdict(int)
    for i in range(len(friends)):
        fri[friends[i]] = i
    
    return fri

def compareWeight(a, b, giftWeight, friendIndexed, nextMonth):
    a = friendIndexed[a]
    b = friendIndexed[b]
    if giftWeight[a] > giftWeight[b]:
        nextMonth[a] += 1
    elif giftWeight[a] < giftWeight[b]:
        nextMonth[b] += 1
        
    return nextMonth

def solution(friends, gifts):
    answer = 0
    friendIndexed = indexing(friends)
    n = len(friends)
    giftWeight = [0 for _ in range(n)]
    comb = combinations(friends, 2)
    nextMonth = [0 for _ in range(n)]
    history = defaultdict(int)
    
    for g in gifts:
        a, b = g.split()
        giftWeight[friendIndexed[a]] += 1
        giftWeight[friendIndexed[b]] -= 1
        history[g] += 1
    
    key = history.keys()
    
    for a, b in comb:
        s1 = a + " " + b
        s2 = b + " " + a
        
        if s1 in key or s2 in key:
            if history[s1] > history[s2]:
                nextMonth[friendIndexed[a]] += 1
            elif history[s1] < history[s2]:
                nextMonth[friendIndexed[b]] += 1
            else:
                nextMonth = compareWeight(a, b, giftWeight, friendIndexed, nextMonth)
        else:
            nextMonth = compareWeight(a, b, giftWeight, friendIndexed, nextMonth)
    
    return max(nextMonth)

fri = ["muzi", "ryan", "frodo", "neo"]
gif = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(fri, gif))
print(solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]))
print(solution(["a", "b", "c"], ["a b", "b a", "c a", "a c", "a c", "c a"]))