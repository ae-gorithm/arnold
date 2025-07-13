import sys
input = sys.stdin.readline

s = input().strip()
n = int(input())
ordA = ord('a')
ordZ = ord('z')

li  = [[0 for _ in range(ordZ-ordA+1)] for _ in range(len(s)+1)]

for i in range(1, len(s)+1):
    li[i] = li[i-1].copy()
    li[i][ord(s[i-1])-97] += 1
        
for _ in range(n):
    ch, start, end = input().split()
    print(li[int(end)+1][ord(ch)-97] - li[int(start)][ord(ch)-97])