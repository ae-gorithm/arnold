import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque()
edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    edges[a].append(b)
    edges[b].append(a)

ans = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dq.append(i)
    visited = [False for _ in range(n+1)]
    visited[i] = True
    weight = 0

    while dq:
        l = len(dq)
        weight += 1
        for _ in range(l):
            cur = dq.popleft()

            for nextNode in edges[cur]:
                if visited[nextNode]: continue

                visited[nextNode] = True
                dq.append(nextNode)
                ans[i] += weight

print(ans.index(min(ans[1:])))