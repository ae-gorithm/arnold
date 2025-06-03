import sys
import heapq
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
visited = [False for _ in range(n+1)]
edge = [[] for _ in range(n+1)]
vertex = [0 for _ in range(n+1)]
cnt = 1
for _ in range(m):
    a, b = map(int, input().split())
    heapq.heappush(edge[b], a)
    heapq.heappush(edge[a], b)

def dfs(node):
    global cnt
    visited[node] = True
    vertex[node] = cnt

    while edge[node]:
        nextNode = heapq.heappop(edge[node])

        if not visited[nextNode]:
            cnt += 1
            visited[nextNode] = True
            dfs(nextNode)
dfs(r)
for i in range(1, n+1):
    print(vertex[i])