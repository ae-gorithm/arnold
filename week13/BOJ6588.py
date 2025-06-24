import sys
input = sys.stdin.readline

l = 1000001
prime = [True for _ in range(l)]
for i in range(2, int(l**0.5)):
    if prime[i]:
        for j in range(i*i, l, i):
            prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(3, n//2+1, 2):
        if prime[i] and prime[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break
    else:
        print("Goldbach's conjecture is wrong.")