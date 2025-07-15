import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
minDp = board.copy()
maxDp = board.copy()

for i in range(1, n):
    board = list(map(int, input().split()))
    min0 = min(board[0] + minDp[0], board[0] + minDp[1])
    min1 = min(board[1] + minDp[0], board[1] + minDp[1], board[1] + minDp[2])
    min2 = min(board[2] + minDp[1], board[2] + minDp[2])

    max0 = max(board[0] + maxDp[0], board[0] + maxDp[1])
    max1 = max(board[1] + maxDp[0], board[1] + maxDp[1], board[1] + maxDp[2])
    max2 = max(board[2] + maxDp[1], board[2] + maxDp[2])

    minDp[0], minDp[1], minDp[2] = min0, min1, min2
    maxDp[0], maxDp[1], maxDp[2] = max0, max1, max2

print(max(maxDp), min(minDp))