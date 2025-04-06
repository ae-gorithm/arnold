import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
edges = [[] for _ in range(n)]
visitedDFS = [False for _ in range(n)]
visitedBFS = [False for _ in range(n)]
ansDFS = []
ansBFS = []

for _ in range(m):
    a, b = map(int, input().split())

    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def dfs(v):
    if visitedDFS[v]:
        return
    ansDFS.append(v+1)
    visitedDFS[v] = True

    for nextNode in sorted(edges[v]):
        dfs(nextNode)

def bfs(v):
    dqBFS = deque([v])

    while dqBFS:
        node = dqBFS.popleft()

        if visitedBFS[node]:
            continue
        ansBFS.append(node+1)
        visitedBFS[node] = True
        for nextNode in sorted(edges[node]):
            dqBFS.append(nextNode)

dfs(v-1)
bfs(v-1)
print(*ansDFS)
print(*ansBFS)