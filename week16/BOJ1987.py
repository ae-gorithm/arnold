import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0 ,-1, 0]

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
ans = 1
s = set(board[0][0])
def dfs(y, x, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n or board[ny][nx] in s:
            continue
        s.add(board[ny][nx])
        dfs(ny, nx, cnt+1)
        s.remove(board[ny][nx])

dfs(0, 0, 1)
print(ans)