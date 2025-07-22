import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())

#   0
# 4 1 5
#   2
#   3
# 주사위가 위와 같이 생겼을 때 배열의 인덱스를 위와 같이 설정한다.

dice = [0, 0, 0, 0, 0, 0]
# dice = ['a', 'b', 'c', 'd', 'e', 'f']

def moveSouth():
    global x
    dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    x += 1

def moveNorth():
    global x
    dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]
    x -= 1

def moveEast():
    global y
    dice[1], dice[5], dice[3], dice[4] = dice[5], dice[3], dice[4], dice[1]
    y += 1

def moveWest():
    global y
    dice[1], dice[4], dice[3], dice[5] = dice[4], dice[3], dice[5], dice[1]
    y -= 1

def canMove(order):
    if order == 1:
        if y == m-1:
            return False
        return True
    elif order == 2:
        if y == 0:
            return False
        return True
    elif order == 3:
        if x == 0:
            return False
        return True
    else:
        if x == n-1:
            return False
        return True

board = [list(map(int, input().split())) for _ in range(n)]
move = ['', 'moveEast()', 'moveWest()', 'moveNorth()', 'moveSouth()']
orders = list(map(int, input().split()))
for order in orders:
    if not canMove(order):
        continue
    exec(move[order])
    if board[x][y] == 0:
        board[x][y] = dice[3]
    else:
        dice[3] = board[x][y]
        board[x][y] = 0
    print(dice[1])