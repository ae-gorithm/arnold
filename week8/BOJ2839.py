import sys
n = int(input())

# [-1, -1, 1, -1, 1, 2, -1, ]

MAX = sys.maxsize
dp = [MAX for _ in range(n+1)]
dp[0] = 0
dp[3] = 1
for i in range(5, n+1):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)
if dp[-1] >= MAX:
    print(-1)
else:
    print(dp[-1])