n = int(input())
nums = list(map(int, input().split()))

dp = nums[:]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], nums[i]+dp[j])

print(max(dp))