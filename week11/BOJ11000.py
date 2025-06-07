import sys
input = sys.stdin.readline
n = int(input())

import heapq
time = [list(map(int, input().split())) for _ in range(n)]
time.sort()

hq = []
heapq.heappush(hq, time[0][0])

for i in range(1, n):
    if hq[0] > time[i][0]:
        heapq.heappush(hq, time[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, time[i][1])

print(len(hq))


# t = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     t.append([a, 1])
#     t.append([b, -1])

# t.sort()
# cnt = 0
# ans = 0
# for loc, val in t:
#     cnt += val
#     ans = max(ans, cnt)

# print(ans)