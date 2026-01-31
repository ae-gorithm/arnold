import heapq
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
n = int(input())
board = []
sharkPosition = []

for i in range(n):
    tmp = list(map(int, input().split()))
    if 9 in tmp:
        sharkPosition.append(i)
        idx = tmp.index(9)
        sharkPosition.append(idx)
        tmp[idx] = 0
    board.append(tmp)
    
sharkSize = 2

def findShortestPos(sharkPosition, sharkSize):
    hq = []
    ret = []
    heapq.heappush(hq, [0, sharkPosition[0], sharkPosition[1]])
    visited = [[False] * n for _ in range(n)]
    
    while hq:
        dist, y, x = heapq.heappop(hq)
        
        if visited[y][x]: continue
        visited[y][x] = True
        
        if (board[y][x] != 0 and board[y][x] < sharkSize):
            return dist, y, x
        
        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[ny][nx] > sharkSize: continue
            
            heapq.heappush(hq, [dist+1, ny, nx])
    return -1, -1, -1


def solution(sharkSize, sharkPosition):
    t = 0
    while True:
        for _ in range(sharkSize):
            nd, ny, nx = findShortestPos(sharkPosition, sharkSize)
            if nd == -1:
                return t
            t += nd
            sharkPosition = [ny, nx]
            board[ny][nx] = 0
            
        sharkSize += 1

print(solution(sharkSize, sharkPosition))