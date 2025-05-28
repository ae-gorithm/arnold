from collections import deque

for i in range(1, 5):
    globals()[f"gear{i}"] = deque(map(int, list(input())))

n = int(input())

def rotate(gear, dir):
    if dir == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())

def findMatch():
    ret = [[] for _ in range(5)]
    for i in range(1, 4):
        if globals()[f"gear{i}"][2] != globals()[f"gear{i+1}"][-2]:
            ret[i].append(i+1)
            if i != 4:
                ret[i+1].append(i)
    return ret

def process(num, dir, rot, visited):
    rotate(globals()[f"gear{num}"], dir)

    visited[num] = True

    for nextNum in rot[num]:
        if not visited[nextNum]:
            process(nextNum, -dir, rot, visited)

for _ in range(n):
    num, dir = map(int, input().split())

    rot = findMatch()
    visited = [False for _ in range(5)]
    visited[num] = True

    process(num, dir, rot, visited)

ans = 0
for i in range(1, 5):
    ans += globals()[f"gear{i}"][0] * 2**(i-1)

print(ans)