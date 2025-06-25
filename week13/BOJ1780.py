import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = [0, 0, 0]
def daq(n, y, x):
    if n == 1:
        val = board[y][x]
        ans[val] += 1
        return
    
    val = board[y][x]
    for i in range(n):
        for j in range(n):
            if board[y+i][x+j] != val:
                for k in range(0, n, n//3):
                    for l in range(0, n, n//3):
                        daq(n//3, k+y, l+x)
                return
    else:
        ans[val] += 1

daq(n, 0, 0)
print(ans[-1])
print(ans[0])
print(ans[1])