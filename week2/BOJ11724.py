import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n+1))
ans = defaultdict(int)
def find(x):
    if parent[x] == x:
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

    union(find(a), find(b))

for node in parent:
    ans[find(node)] += 1

print(len(ans.keys())-1)