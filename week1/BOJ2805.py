import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2

    h = 0
    for i in range(n):
        if trees[i] > mid:
            h += trees[i] - mid

    if h >= m:
        start = mid+1

    if h < m:
        end = mid-1

print(end)
# 1 20 -> 10
# 10 + 5 + 0 + 7 > 7
# 10 20 -> 15
# 5 0 0 2 == 7

# 1 46 -> 23
# 0 19 17 3 23 > 20
# 23 46 -> 34
# 0 8 6 0 12 > 20
# 34 46 -> 40
# 0 2 0 0 6 < 20
# 34 40 -> 37
# 0 5 3 0 9 < 20
# 34 37 -> 35
# 0 7 5 0 11 > 20
# 35 37 -> 36
# 0 6 4 0 10 == 20

# 1 46 -> 23
# 0 19 17 3 23 > 21
# 23 46 -> 34
# 0 8 6 0 12 > 21
# 34 46 -> 40
# 0 2 0 0 6 < 21
# 34 40 -> 37
# 0 5 3 0 9 < 21
# 34 37 -> 35
# 0 7 5 0 11 > 21
# 35 37 -> 36
# 0 6 4 0 10 < 21
# 35 36 -> 35
# 0 7 5 0 11 > 21
