from itertools import product
def solution(n, info):
    answer = [-1]
    info.reverse()
    maxRes = 0
    for results in product((True, False), repeat=11):
        s = 0
        for i in range(11):
            if results[i]:
                s += info[i]+1
        if s <= n:
            apeach = 0
            ryan = 0
            for i in range(11):
                if info[i] and not results[i]:
                    apeach += i
            for i in range(11):
                if results[i]:
                    ryan += i
            res = ryan - apeach
            if res > maxRes:
                maxRes = res
                answer = [info[i]+1 if results[i] else 0 for i in range(11)]
                answer[0] = n-s
    answer.reverse()
    return answer

#   10  9  8  7  6  5  4  3  2  1  0
