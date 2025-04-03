h, w = map(int, input().split())
board = list(map(int, input().split()))

ans = 0

for i in range(1, w-1):
    start = max(board[:i])
    end = max(board[i:])

    standard = min(start, end)
    if standard > board[i]:
        ans += standard - board[i]

print(ans)