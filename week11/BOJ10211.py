import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1, n):
        nums[i] += nums[i-1]

    nums = [0] + nums
    ans = -sys.maxsize

    for i in range(1, n+1):
        for j in range(i):
            ans = max(nums[i]-nums[j], ans)
    print(ans)