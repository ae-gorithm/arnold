import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
edge = [[] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        if li[j] == 1:
            edge[i].append(j)

for curNode in range(n):
    dq = deque([curNode])

    while dq:
        cur = dq.popleft()
        for nextNode in edge[cur]:
            if ans[curNode][nextNode] == 0:
                ans[curNode][nextNode] = 1
                dq.append(nextNode)

for i in range(n):
    print(*ans[i])
