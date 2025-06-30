import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
weight = [0 for _ in range(n+1)]
for i in range(1, n):
    graph[parent[i]].append(i+1)

for _ in range(m):
    person, praise = map(int, input().split())
    weight[person] += praise

dq = deque([1])

while dq:
    curNode = dq.popleft()

    for nextNode in graph[curNode]:
        weight[nextNode] += weight[curNode]
        dq.append(nextNode)

print(*weight[1:])