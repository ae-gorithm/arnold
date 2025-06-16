import sys
input = sys.stdin.readline

n, m ,k = map(int, input().split())
fee = list(map(int, input().split()))
parent = [i for i in range(n+1)]

def find(x):
    if x == parent[x]:
        return parent[x]
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if fee[a-1] > fee[b-1]: parent[a] = b
    else: parent[b] = a

for _ in range(m):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)

s = set()
for i in parent:
    s.add(find(i))
ans = 0
for value in s:
    if value != 0:
        ans += fee[value-1]

if ans > k:
    print("Oh no")
else:
    print(ans)