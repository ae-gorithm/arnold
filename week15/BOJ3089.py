import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = [int(input()) for _ in range(n)]

start = 1
end = max(li) * m
lower = set()

def biSearch(start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0

        if mid == start or mid == end:
            if start in lower:
                return end
            else:
                return start

        for ti in li:
            total += mid//ti
            if total >= m:
                end = mid
                break
        else:
            start = mid
            lower.add(mid)
    
print(biSearch(start, end))

# 3 8 3 6 9 2 4
# 2 3 3 4 6 8 9

# 1, 90 -> 45
# 22, 15, 15, 11, 7, 5, 5 > 10
# 1, 45 -> 23
# 11, > 10
# 1, 23 -> 12
# 6, 4 > 10
# 1, 12 -> 6
# 3, 2, 2, 1, 1, 0, 0 < 10
# 6, 12 -> 9
# 4, 3, 3, 2, 1, 1, 1 > 10
# 6, 9 -> 7
# 3, 2, 2, 1, 1, 0, 0 < 10
# 7, 9 -> 8
# 4, 2, 2, 2, 1, 1, 1 > 10
# 7, 8 -> 7