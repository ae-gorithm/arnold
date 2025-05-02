a = int(input())
dp = [-1 for _ in range(a+1)]

for i in range(1, a+1):
    if 30 % (i+1) == 0:
        print(i)