import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
comb = list(combinations(range(1, n+1), n//2))
ans = sys.maxsize

for i in range(len(comb)//2):
    start = comb[i]
    link = comb[-i-1]
    startComb = list(combinations(start, 2))
    linkComb = list(combinations(link, 2))
    
    startExp = 0
    linkExp = 0
    for a, b in startComb:
        a -= 1
        b -= 1
        startExp += board[a][b]
        startExp += board[b][a]
    for a, b in linkComb:
        a -= 1
        b -= 1
        linkExp += board[a][b]
        linkExp += board[b][a]
    
    ans = min(ans, abs(startExp - linkExp))

print(ans)

# 123 456
# 124 356
# 125 346
# 126 345
# 134 256