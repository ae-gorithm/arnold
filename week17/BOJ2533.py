import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[1, 0] for _ in range(n+1)]

level = []

dq = deque([1])
visited = [False for _ in range(n+1)]
visited[1] = True

while dq:
    parent = dq.popleft()

    for child in tree[parent]:
        if visited[child]: continue

        level.append([parent, child])
        dq.append(child)
        visited[child] = True

while level:
    parent, child = level.pop()
    
    dp[parent][0] += min(dp[child])
    dp[parent][1] += dp[child][0]

print(min(dp[1]))