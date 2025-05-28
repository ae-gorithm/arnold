n, k = map(int, input().split())
prime = [True for _ in range(n+1)]
cnt = 0
for i in range(2, n+1):
    if prime[i]:
        for j in range(i, n+1, i):
            if prime[j]:
                cnt += 1
            prime[j] = False

            if cnt == k:
                print(j)
                exit()
