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

# a = 2**(math.ceil(math.log2(n)))

def next_power_of_two(n):
    if n <= 0:
        return 1
    if n & (n - 1) == 0:
        return n  # 이미 2의 거듭제곱이면 그대로
    return 1 << n.bit_length()

a = next_power_of_two(n)
print(2*n - a)