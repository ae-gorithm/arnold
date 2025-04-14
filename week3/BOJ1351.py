n, p, q = map(int, input().split())

dp = {0 : 1}

def dfs(n):
    global ans

    if dp.get(n) != None:
        return dp[n]
    
    dp[n] = dfs(n//p) + dfs(n//q)
    return dp[n]

dfs(n)
print(dp[n])

# 7 2 3

# dp[7] = dp[3] + dp[2]
# dp[3] = dp[1] + dp[0]
# dp[2] = dp[1] + dp[0]
# dp[1] = dp[0] + dp[0]
# dp[0] = 1