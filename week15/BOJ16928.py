import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [i for i in range(101)]
visited = [False for _ in range(101)]
for _ in range(n+m):
    a, b = map(int, input().split())
    board[a] = b

def bfs():
    dq = deque()
    dq.append(1)
    ans = 0
    while dq:
        l = len(dq)

        for _ in range(l):
            cur = dq.popleft()

            if cur == 100:
                return ans

            if visited[cur]: continue
            visited[cur] = True
            for i in range(1, 7):
                if cur+i < 101:
                    dq.append(board[cur+i])
        ans += 1

print(bfs())