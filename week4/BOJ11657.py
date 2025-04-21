import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
distance = [sys.maxsize for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

distance[1] = 0
for i in range(1, n+1):
    for j in range(m):
        curNode = graph[j][0]
        nextNode = graph[j][1]
        nextCost = graph[j][2]

        if distance[curNode] != sys.maxsize and distance[nextNode] > distance[curNode] + nextCost:
            distance[nextNode] = distance[curNode] + nextCost

            if i == n:
                print(-1)
                exit()

for i in range(2, n+1):
    if distance[i] != sys.maxsize:
        print(distance[i])
    else:
        print(-1)