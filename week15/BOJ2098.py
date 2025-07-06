import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[sys.maxsize for _ in range(2**n)] for _ in range(n)]
ans = [sys.maxsize for _ in range(n)]
def tsp(idx, visit):
    dq = deque([[idx, visit]])
    dp[idx][visit] = 0

    while dq:
        cur, route = dq.popleft()

        if route == 2**n - 1:
            if board[cur][idx] != 0:
                ans[cur] = min(ans[cur], dp[cur][route] + board[cur][idx])
            else:
                dp[cur][route] = sys.maxsize
            continue

        for i in range(n):
            if board[cur][i] == 0 or route & (1 << i) != 0: continue
            if dp[i][route | (1 << i)] > dp[cur][route] + board[cur][i]:
                dp[i][route | (1 << i)] = dp[cur][route] + board[cur][i]
                dq.append([i, route|(1 << i)])
tsp(0, 1)
print(min(ans))