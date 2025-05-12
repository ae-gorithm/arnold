import heapq
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        if num < 0:
            heapq.heappush(hq, [-num, num])
        else:
            heapq.heappush(hq, [num, num])