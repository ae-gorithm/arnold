import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    weight, value = stuff[i]
    for j in range(1, m+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[-1][-1])