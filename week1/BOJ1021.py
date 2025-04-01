from collections import deque
n, m = map(int, input().split())
nums = deque(map(int, input().split()))
ns = deque(range(1, n+1))
left = 0
right = 0
cnt = 0

while nums:
    if nums[0] == ns[left] or nums[0] == ns[right]:
        while ns[0] != nums[0]:
            ns.append(ns.popleft())
            left = 0
            right = 0
        ns.popleft()
        nums.popleft()
        continue
    cnt += 1
    left = (left + 1) % len(ns)
    right -= 1

print(cnt)