import sys
from collections import Counter
input = sys.stdin.readline
n, h = map(int, input().split())
imos = [0 for _ in range(h+2)]

for i in range(n):
    a = int(input())

    if i % 2 == 0:
        imos[1] += 1
        imos[a+1] -= 1
    else:
        imos[h+1] -= 1
        imos[h-a+1] += 1

for i in range(1, h+1):
    imos[i] += imos[i-1]

ansMin = min(imos[1:h+1])
ansNum = 0
for i in range(1, h+1):
    if imos[i] == ansMin:
        ansNum += 1

print(ansMin, ansNum)