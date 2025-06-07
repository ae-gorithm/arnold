# 1 2 2 4 2 4 6 8 2 4 6 8 10 12 14 16
import math
n = int(input())
# dq = deque([i for i in range(1, n+1)])

# while len(dq) != 1:
#     dq.popleft()
#     dq.append(dq.popleft())

# print(dq[0])
# ------------------------
# a = 1
# while n > a:
#     a *= 2

# print(a - 2*(a - n))
# -------------------------

a = 2**(math.ceil(math.log2(n)))
print(2*n - a)