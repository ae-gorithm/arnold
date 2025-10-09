from collections import defaultdict

def solution(orders, course):
    answer = []
    d = defaultdict(int)
    for order in orders:
        visited = [False for _ in range(len(order))]
        for c in course:
            comb(sorted(order), c, 0, "", d, visited, 0)
    kv = list(d.items())
    kv.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))
    print(kv)
    answer = findAnswer(kv)
    return answer

def findAnswer(kv):
    answer = []
    ansToBin = []
    length = [0 for _ in range(11)]
    
    for k, v in kv:
        if v == 1: break
        
        if length[len(k)] <= v:
            length[len(k)] = v
        else:
            continue
        
        kToBin = 0
        for ch in k:
            kToBin += 2**(97-ord(ch))
        for ans in ansToBin:
            if k & ans == k:
                break
        else:
            answer.append(k)
    return sorted(answer)
    
def comb(order, t, depth, s, d, visited, start):
    if t == depth:
        d[s] += 1
        return
    
    for i in range(start, len(order)):
        if not visited[i]:
            visited[i] = True
            s += order[i]
            comb(order, t, depth+1, s, d, visited, i+1)
            visited[i] = False
            s = s[:-1]
# 최대 10!
# * 20