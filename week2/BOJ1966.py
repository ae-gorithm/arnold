import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    nums = deque(map(int, input().split()))
    docs = deque(range(n))

    ans = 1

    while True:
        if len(nums) == 0:
            break
        if nums[0] == max(nums):
            if docs[0] == m:
                break
            else:
                ans += 1
                nums.popleft()
                docs.popleft()
        else:
            nums.append(nums.popleft())
            docs.append(docs.popleft())
    print(ans)