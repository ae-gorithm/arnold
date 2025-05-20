n = int(input())
nums = set(list(map(int, input().split())))
m = int(input())
wnums = list(map(int, input().split()))

for num in wnums:
    if num in nums:
        print(1)
    else:
        print(0)