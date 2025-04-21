import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [0 ,1 ,0 ,-1]
dy = [1, 0, -1, 0]

def bfs(y, x, team):
    dq = deque()
    ret = 1

    dq.append([y, x])
    visited[y][x] = True

    while dq:
        y, x = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n or visited[ny][nx] or board[ny][nx] != team:
                continue
            
            visited[ny][nx] = True
            dq.append([ny, nx])
            ret += 1
    return ret

pd = {'W' : 0, 'B' : 0}
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            power = bfs(i, j, board[i][j])
            pd[board[i][j].upper()] += power**2

print(*pd.values())