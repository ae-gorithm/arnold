import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []

def find(x):
    if x == parent[x]:
        return parent[x]
    
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else: 
        parent[a] = b

ans = 0
# for _ in range(m):
#     edges.append(list(map(int, input().split())))

# for i in range(m):
#     a, b = edges[i]
#     if find(a) != find(b):
#         union(a, b)
#     else:
#         print(i+1)
#         break
# else:
#     print(0)

for i in range(m):
    a, b = map(int, input().split())
    if find(a) != find(b):
        union(a, b)
    else:
        print(i+1)
        break
else:
    print(0)