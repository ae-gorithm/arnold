import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for i in range(n):
    distance[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())

    distance[a-1][b-1] = min(distance[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(n):
    for j in range(n):
        if distance[i][j] == sys.maxsize:
            distance[i][j] = 0
    print(*distance[i])