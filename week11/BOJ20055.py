from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

belt = deque(map(int, input().split()))
robot = deque([False for _ in range(2*n)])
cnt = 0
ans = 0

def rotateBelt():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    robot[n-1] = False

def moveRobot():
    global cnt
    for i in range(n-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] > 0:
            robot[i+1] = True
            robot[i] = False
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    robot[n-1] = False

def putRobot():
    global cnt
    if not robot[0] and belt[0] > 0:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

while True:
    if cnt >= k:
        break
    ans += 1
    rotateBelt()
    moveRobot()
    putRobot()
print(ans)
# 1 2 1 2 1 2
#
# 2 1 2 1 2 1
# 
# 1 1 2 1 2 1
# r

# 1 1 1 2 1 2
#   r
# 1 1 0 2 1 2
#     r
# 0 1 0 2 1 2
# r 1 r 2 1 2