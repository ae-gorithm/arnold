import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]
edges = []

for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(edges, [c, a, b])

def find(x):
    if x == parent[x]:
        return parent[x]
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b: parent[b] = a
    else: parent[a] = b

ans = 0

while edges:
    c, a, b = heapq.heappop(edges)

    if find(a) != find(b):
        union(a, b)
        ans += c

print(ans)