import sys
input = sys.stdin.readline

def find(x, parent):
    if parent[x] == x:
        return parent[x]

    parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)

    if a < b: parent[b] = a
    else: parent[a] = b

c = 1
while True:
    n, m = map(int, input().split())
    
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())

        if find(a, parent) != find(b, parent):
            union(a, b, parent)
        else:
            union(a, 0, parent)
            union(b, 0, parent)
    
    ans = set()
    for val in parent:
        ans.add(find(val, parent))
    l = len(ans)
    if l == 1:
        print("Case {}: No trees.".format(c))
    elif l == 2:
        print("Case {}: There is one tree.".format(c))
    elif l > 2:
        print("Case {}: A forest of {} trees.".format(c, l-1))

    
    c += 1
