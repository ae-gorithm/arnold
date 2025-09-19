from collections import deque
def solution(n, k):
    answer = 0
    kBase = intToKbase(n, k)
    intArr = kBase.split("0")
    for value in intArr:
        if value != "":
            if isPrime(int(value)):
                print(int(value))
                answer += 1
    return answer

def intToKbase(n, k):
    strArr = deque()
    while n >= k:
        strArr.appendleft(str(n%k))
        n//=k
    strArr.appendleft(str(n))
    return ''.join(list(strArr))

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
    
# 0으로 split
# 나올 수 있는 소수의 최댓값?