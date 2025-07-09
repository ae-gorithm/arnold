import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [0 for _ in range(101)]

for i in range(n):
    for j in range(100, L[i]-1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])

print(dp[99])