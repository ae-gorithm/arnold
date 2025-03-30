import sys
n = int(input())

dp = [sys.maxsize for _ in range(n+1)]
dp[0] = 0
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])
# dp?
# 1 2 3 4 5 6 7 8 9 10
# 0 1 1 
# 0 1 1 2 
# 0 1 1 2 3 
# 0 1 1 2 3 2
# 0 1 1 2 3 2 3
# 0 1 1 2 3 2 3 3
# 0 1 1 2 3 2 3 3 2
# 0 1 1 2 3 2 3 3 2 3