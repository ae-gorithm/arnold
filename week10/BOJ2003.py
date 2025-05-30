n, m = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
sumn = nums[0]
nums += [0]
ans = 0
while end < n:
    if sumn == m:
        ans += 1
        end += 1
        sumn += nums[end]
    elif sumn > m:
        sumn -= nums[start]
        start += 1
    else:
        end += 1
        sumn += nums[end]
        
print(ans)

# 100,000,000