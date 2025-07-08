from collections import Counter
n = int(input())
li = list(map(int, input().split()))

l = 0
r = 1
ans = 0
f = [0 for _ in range(10)]
f[li[l]] += 1
while l < n and r <= n:
    counter = Counter(f)
    if counter[0] > 7 and r <= n:
        ans = max(ans, r-l)
        if r < n:
            f[li[r]] += 1
        r += 1
    else:
        f[li[l]] -= 1
        l += 1

print(ans)

# from collections import deque
# dq = deque()
# dq.append(li[0])
# f[li[0]] += 1
# ans = 1
# idx = 1
# while dq:
#     counter = Counter(f)
#     if counter[0] > 7 and idx <= n:
#         ans = max(ans, len(dq))
#         if idx < n:
#             dq.append(li[idx])
#             f[li[idx]] += 1
#         idx += 1
#     else:
#         f[dq.popleft()] -= 1
        
# print(ans)



# 1 2 3 1 2 3
# 1 1 1 2 2 3 3