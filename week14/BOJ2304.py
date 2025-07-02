import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
loc = 0
maxH = 0
li.sort()

for i in range(n):
    l, m = li[i]
    if m > maxH:
        loc = i
        maxH = m

lastLoc = li[0][0]
lastMax = li[0][1]
ans = 0
for i in range(loc+1):
    a, b = li[i]
    if lastMax < b:
        ans += (a - lastLoc) * lastMax
        lastMax = b
    else:
        ans += (a - lastLoc) * lastMax
    lastLoc = a
lastLoc = li[-1][0]
lastMax = li[-1][1]
for i in range(n-1, loc-1, -1):
    a, b = li[i]
    if lastMax < b:
        ans += (lastLoc - a) * lastMax
        lastMax = b
    else:
        ans += (lastLoc - a) * lastMax
    lastLoc = a

print(ans + maxH)