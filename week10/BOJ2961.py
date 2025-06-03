import sys
n = int(input())
flavour = [list(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

for i in range(1, 2**n):
    b = format(i, 'b').zfill(n)
    valB = 1
    valS = 0
    for j in range(len(b)):
        if b[j] == '1':
            valB *= flavour[j][0]
            valS += flavour[j][1]
    ans = min(ans, abs(valB - valS))
    
print(ans)