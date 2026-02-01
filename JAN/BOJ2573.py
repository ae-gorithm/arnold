from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def countIce():
    global visited
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    return cnt

def bfs(y, x):
    global visited
    dq = deque()
    dq.append([y, x])
    visited[y][x] = True
    
    while dq:
        cy, cx = dq.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if board[ny][nx] == 0 or visited[ny][nx]:
                continue
            
            visited[ny][nx] = True
            dq.append([ny, nx])

def melt():
    global board
    newBoard = [row.copy() for row in board]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if board[i][j] != 0:
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    
                    if board[ny][nx] == 0 and newBoard[i][j] > 0:
                        newBoard[i][j] -= 1
    board = [row.copy() for row in newBoard]
            
ans = 0
while True:
    ret = countIce()
    if ret > 1:
        print(ans)
        break
    elif ret == 1:
        ans += 1
    else:
        print(0)
        break
    melt()

# 0 0 0
# 0 0 0
# 0 0 0