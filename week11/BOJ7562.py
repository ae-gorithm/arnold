import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
d = [[-2, -1], [-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1]]

def bfs(dq, visited, n, destX, destY):
    ans = 0
    while dq:
        l = len(dq)

        for _ in range(l):
            y, x = dq.popleft()
            visited[y][x] = True
            if y == destY and x == destX:
                return ans

            for i in range(8):
                nx = x + d[i][1]
                ny = y + d[i][0]

                if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[ny][nx]:
                    continue
                visited[ny][nx] = True
                dq.append([ny, nx])
        ans += 1

for _ in range(T):
    l = int(input())
    cur = list(map(int, input().split()))
    dest = list(map(int, input().split()))

    visited = [[False for _ in range(l)] for _ in range(l)]

    print(bfs(deque([cur]), visited, l, dest[1], dest[0]))