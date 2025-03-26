import sys
input = sys.stdin.readline

n, l = map(int, input().split())

pipes = sorted(list(map(int, input().split())))
ans = 0
start = 0
end = 0
while end < n:
    if pipes[end] - pipes[start] < l:
        end += 1
    else:
        ans += 1
        start = end
        

if (end != start):
    ans += 1
print(ans)

# 투 포인터 사용
# [1, 2, 100, 101]
#  ㅗ
#         ㅗ

# [1, 2, 100, 101]
#         ㅗ
#         ㅗ