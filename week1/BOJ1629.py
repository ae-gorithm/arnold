import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def mult(a, b):
    if b == 1:
        return a%c
    
    if b % 2 == 0:
        return mult(((a%c)*(a%c))%c, b//2)
    else:
        return mult(((a%c)*(a%c))%c, b//2) * a%c
    
print(mult(a, b))

# a를 b번 곱 -> a^b
# -> (a*a) * (a*a) * ...
# -> (a2*a2) * (a2*a2) * ... a2 = a*a

# (a * b) % c = (a%c * a%c) % c

# (10 10) (10 10) (10 10) (10 10) (10 10) 10
# ((10 10) (10 10)) ((10 10) (10 10)) 10 10 10

# b = 11
# (10 10) (10 10) (10 10) (10 10) (10 10) 10

# b = 5
# ((100 100) (100 100) 100) 10

# b = 2
# ((10000 10000) 100) 10

# b = 1
# 10000000000 100 10

# def mult(a, b):
#     if b == 1:
#         return a%c
    
#     if b % 2 == 0:
#         return mult(a*a, b//2)
#     else:
#         return mult(a*a, b//2) * a