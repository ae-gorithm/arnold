import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)] # 학생들의 자리를 지정할 배열
empty = [[4 for _ in range(n)] for _ in range(n)] # 비어있는 자리를 나타낼 배열. board에 학생이 들어갈 때 마다 그 위치의 상하좌우에 -1이 됨
likeFriend = [[] for _ in range(n**2 + 1)] # index의 학생이 좋아하는 학생들의 번호가 있는 배열
for i in range(n): # 빈 좌석의 테두리 부분을 -1, 꼭지점은 -2
    empty[i][0] -= 1
    empty[0][i] -= 1
    empty[n-1][i] -= 1
    empty[i][n-1] -= 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def makeBoard(student, likes):
    like = [[0 for _ in range(n)] for _ in range(n)]
    maxEmpty = -1
    maxLike = -1
    locX, locY = n, n
    for y in range(n-1, -1, -1):
        for x in range(n-1, -1, -1):
            if board[y][x] != 0: # 이미 좌석을 차지하고 있는 학생이 있으면 continue
                continue

            for i in range(4): # 상하좌우에 학생이 있는 지를 체크
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[ny][nx] in likes: # 상하좌우에 있는 학생이 좋아하는 학생이면 해당 좌석의 likeCount 증가
                    like[y][x] += 1

            if like[y][x] > maxLike:
                locX, locY = x, y
                maxLike = like[y][x]
                maxEmpty = empty[y][x] # maxLike는 높은데 maxEmpty가 작을 수 있으므로 갱신해야 함
                
            if like[y][x] == maxLike and empty[y][x] >= maxEmpty:
                locX, locY = x, y
                maxEmpty = empty[y][x]

    board[locY][locX] = student
    minusEmpty(locX, locY) # 사람 한 명을 좌석에 배치하면 empty 배열에서 그 위치의 상하좌우에 -1

def minusEmpty(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        empty[ny][nx] -= 1

for _ in range(n**2):
    li = list(map(int, input().split()))

    likeFriend[li[0]] = li[1:]
    makeBoard(li[0], li[1:])

ans = 0
satisfying = [0, 1, 10, 100, 1000]
for y in range(n): # 만족도 계산
    for x in range(n):
        student = board[y][x]
        value = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[ny][nx] in likeFriend[student]:
                value += 1
        ans += satisfying[value]
print(ans)