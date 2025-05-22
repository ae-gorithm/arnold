import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# wall_loc = []

# def dfs(tmp, a, b):
#     if len(tmp) == 3:
#         wall_loc.append(tmp.copy())
#         tmp.pop()
#         return

#     for i in range(a, n):
#         for j in range(b, m):
#             if board[i][j] == 0 and [i, j] not in tmp:
#                 tmp.append([i, j])
#                 dfs(tmp, i, b)
#                 if tmp:
#                     tmp.pop()

# dfs([], 0, 0)
# print(len(wall_loc))

coord0 = []
virus_loc = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            coord0.append([i, j])
        if board[i][j] == 2:
            virus_loc.append([i, j])

numOf0 = len(coord0)-3
wall_loc = combinations(coord0, 3)

def switch(board, li):
    x = li[1]
    y = li[0]
    board[y][x] = 1

def bfs(li, numOf0):
    dq = deque(virus_loc)
    
    while dq:
        y, x = dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n or li[ny][nx] != 0:
                continue

            li[ny][nx] = 2
            dq.append([ny, nx])
            numOf0 -= 1

    return numOf0

ans = 0

for loc in wall_loc:
    a = loc[0]
    b = loc[1]
    c = loc[2]
    board_copy = [li[:] for li in board]

    switch(board_copy, a)
    switch(board_copy, b)
    switch(board_copy, c)
    ans = max(bfs(board_copy, numOf0), ans)

print(ans)