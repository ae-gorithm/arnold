import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
indegree = [0 for _ in range(n+1)]
dq = deque()
edge = [[] for _ in range(n+1)]
for _ in range(m):
    li = list(map(int, input().split()))

    for i in range(2, li[0]+1):
        indegree[li[i]] += 1
        edge[li[i-1]].append(li[i])

for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)
ans = []
while dq:
    node = dq.popleft()
    ans.append(node)
    for nextNode in edge[node]:
        indegree[nextNode] -= 1
        if indegree[nextNode] == 0:
            dq.append(nextNode)
if len(ans) != n:
    print(0)
else:
    for a in ans:
        print(a)