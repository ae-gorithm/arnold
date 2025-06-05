import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(start):
    dq = deque([[start, 1]])

    while dq:
        tmp = dq.popleft()
        node = tmp[0]
        value = tmp[1]
        
        vertexes[node] = value

        for nextNode in edges[node]:
            if vertexes[nextNode] == value:
                return False
            if vertexes[nextNode] == 0:
                dq.append([nextNode, -value])
    return True

for _ in range(T):
    v, e = map(int, input().split())
    
    edges = [[] for _ in range(v+1)]
    vertexes = [0 for _ in range(v+1)]

    for _ in range(e):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    
    for i in range(1, len(vertexes)):
        if vertexes[i] == 0:
            if not bfs(i):
                print("NO")
                break
    else:
        print("YES")