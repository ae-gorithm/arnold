import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
parent = [i for i in range(n+1)]

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

for _ in range(m):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)

ans = 0

for i in range(2, n+1):
    if find(i) == 1:
        ans+=1

print(ans)