T = int(input())
for _ in range(T):
    n = int(input())
    b = list(str(bin(n))[2:])
    l = len(b)
    b.reverse()
    for i in range(l):
        if b[i] == '1':
            print(i)
