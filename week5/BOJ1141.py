n = int(input())
strs = [input() for _ in range(n)]
strs.sort()

ans = n
for i in range(n):
    for j in range(i+1, n):
        if strs[j].startswith(strs[i]):
            ans -= 1
            break

print(ans)