prime = [True for _ in range(123456*2 +1)]

for i in range(2, int((2*123457)**(1/2))):
    if prime[i]:
        for j in range(i*i, 2*123457, i):
            prime[j] = False

while True:
    n = int(input())
    ans = 0
    if n == 0:
        break

    for i in range(n+1, 2*n + 1):
        if i > 123456*2:
            break
        if prime[i]:
            ans += 1
    print(ans)