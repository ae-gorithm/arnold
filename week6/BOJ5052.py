from collections import defaultdict
T = int(input())

for _ in range(T):
    d = defaultdict(list)
    n = int(input())

    nums = []
    for i in range(n):
        nums.append(input())

    nums.sort()

    for i in range(1, n):
        if nums[i].startswith(nums[i-1]):
            print("NO")
            break
    else:
        print("YES")