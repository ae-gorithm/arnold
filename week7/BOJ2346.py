from collections import deque
n = int(input())
dq = deque(map(int, input().split()))
idx = deque(range(1, n+1))

def moveLeft(n):
    for _ in range(n):
        dq.appendleft(dq.pop())
        idx.appendleft(idx.pop())

def moveRight(n):
    for _ in range(n):
        dq.append(dq.popleft())
        idx.append(idx.popleft())

while dq:
    nextNode = dq.popleft()
    print(idx.popleft())

    if not dq:
        break
    if nextNode > 0:
        moveRight(nextNode-1)
    elif nextNode < 0:
        moveLeft(-1*nextNode)
    else:
        continue