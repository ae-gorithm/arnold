import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance = [sys.maxsize for _ in range(n+1)]
distance[k] = 0

hq = [[0, k]]


while hq:
    info = heapq.heappop(hq)
    cost = info[0]
    node = info[1]

    if distance[node] < cost:
        continue

    for info2 in graph[node]:
        nextNode = info2[0]
        nextCost = info2[1]

        if distance[nextNode] > distance[node] + nextCost:
            distance[nextNode] = distance[node] + nextCost
            heapq.heappush(hq, [distance[node] + nextCost, nextNode])

for i in range(1, n+1):
    if distance[i] != sys.maxsize:
        print(distance[i])
    else:
        print("INF")
