from collections import defaultdict
from itertools import chain
def findCreateVertex(edges, n, nodes):
    s = nodes.copy()
    outDegree = [0 for _ in range(n)]
    
    for start, end in edges:
        if end in s:
            s.remove(end)
        outDegree[start] += 1
    
    ans = 0
    for v in s:
        if outDegree[v] > outDegree[ans]:
            ans = v
    return ans

def setNode(edges):
    s = set()
    for start, end in edges:
        s.add(start)
        s.add(end)
    return s

def solution(edges):
    answer = [0, 0, 0, 0]
    n = max(list(chain.from_iterable(edges)))+1
    nodes = setNode(edges)
    createVertex = findCreateVertex(edges, n, nodes)
    numOfGraph = 0
    inDegree = [0 for _ in range(n)]
    
    for start, end in edges:
        if start != createVertex:
            inDegree[end] += 1
        else:
            numOfGraph += 1
    
    
    cnt = defaultdict(int)
    for node in nodes:
        cnt[inDegree[node]] += 1
    answer[0] = createVertex
    answer[2] = cnt[0]-1
    answer[3] = cnt[2]
    answer[1] = numOfGraph - answer[2] - answer[3]
    
    return answer

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
print(solution([[2, 3], [4, 3], [1, 5], [2, 1]]))
print(solution([[2, 3], [2, 1], [1, 1], [3, 3]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]))
print(solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8], [4, 13], [13, 14], [14, 15], [15, 13]]))