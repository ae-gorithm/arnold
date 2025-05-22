import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

computers = [[] * i for i in range(n+1)]
visited = [False] * (n+1)
q = deque()

def bfs():
    ans = 0
    q.appendleft(1)
    visited[1] = True
    
    while q :
        no = q.popleft()
        
        for i in computers[no] :
            if not visited[i] :
                q.appendleft(i)
                visited[i] = True
                ans += 1
    return ans

for _ in range(m):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

print(bfs())
