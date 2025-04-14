import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

parent = list(range(n+1))
def find(x):
    if parent[x] == x:
        return parent[x]
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b : parent[b] = a
    else : parent[a] = b

for _ in range(m):
    o, a, b = map(int, input().split())

    if o == 0:
        union(find(a), find(b))
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")