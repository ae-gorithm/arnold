import sys
input = sys.stdin.readline

n = int(input())
enter = {}
exit = []
for i in range(n):
    s = input().strip()
    enter[s] = i

for i in range(n):
    s = input().strip()
    exit.append(enter[s])

ans = 0

for i in range(n-1):
    for j in range(i+1, n):
        if exit[i] > exit[j]:
            ans += 1
            break
print(ans)
        
# 1번 테케
# 1
# 2
# 3
# 4

# 4
# 1
# 2
# 3

# 2번 테케
# 1
# 2
# 3
# 4
# 5

# 2
# 5
# 4
# 1
# 3

# 3번 테케
# 1
# 2
# 3
# 4
# 5

# 5
# 3
# 1
# 2
# 4

# 추가 테케
# 1
# 3
# 2
# 4
# 5

# 2
# 1
# 4
# 3
# 5