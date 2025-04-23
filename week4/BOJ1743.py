import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1


def bfs(x, y):
    dq = deque()
    dq.append([x, y])
    cnt = 0

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n or board[ny][nx] == 0:
                continue
            board[ny][nx] = 0
            cnt += 1
            dq.append([nx, ny])
    return cnt

ret = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            ret = max(ret, bfs(j, i))

print(ret)