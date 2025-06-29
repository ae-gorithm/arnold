board = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
ans = 26

def isAttachPossible(y, x, size):
    if x + size > 10 or y + size > 10:
        return False
    
    for i in range(y, y+size):
        for j in range(x, x+size):
            if board[i][j] == 0:
                return False
    
    return True

def attach(y, x, size, value):
    for i in range(y, y+size):
        for j in range(x , x+size):
            board[i][j] = value
    if value == 0:
        papers[size] -= 1
    if value == 1:
        papers[size] += 1

def back(y, x, size):
    global ans
    if 25-sum(papers) >= ans:
        return

    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                for k in range(5, 0, -1):
                    if isAttachPossible(i, j, k) and papers[k] > 0:
                        attach(i, j, k, 0)
                        back(i, j, k)
                        attach(i, j, k, 1)
                return

    ans = min(ans, 25-sum(papers))

back(0, 0, 0)
if ans == 26:
    print(-1)
else:
    print(ans)