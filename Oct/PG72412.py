from itertools import product
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    n = len(info)
    d = getComb(info)
    
    for q in query:
        q = q.replace(" and ", " ").split()
        queryInfo = ''.join(q[:-1])
        queryScore = int(q[-1])
        scores = d[queryInfo]
        ans = len(scores) - bisect.bisect_left(scores, queryScore)
        answer.append(ans)

    return answer

def getComb(info):
    b = ['-', '-', '-', '-']
    ret = defaultdict(list)
    for s in info:
        a = s.split()
        prod = product(*zip(a[:-1], b))
        for value in prod:
            st = ''.join(value)
            ret[st].append(int(a[-1]))
    for key in ret:
        ret[key].sort()
    return ret