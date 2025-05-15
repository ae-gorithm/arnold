import sys
input = sys.stdin.readline
dy = [1, 0, -1 ,0]
dx = [0, 1, 0 ,-1]
n, m, r = map(int, input().split())

li = [list(map(int, input().split())) for _ in range(n)]

def rotate(li):
    ret = [[0 for _ in range(m)] for _ in range(n)]

    layer = min(n, m) // 2
    for l in range(layer):
        y, x = l, l
        tmp = []
        d = 0
        while True:
            tmp.append([y, x])

            ny = y + dy[d]
            nx = x + dx[d]

            if ny < l or ny >= n-l or nx < l or nx >= m-l:
                d += 1
                if d == 4 :
                    break
                ny = y + dy[d]
                nx = x + dx[d]
            y, x = ny, nx
        
        for i in range(len(tmp)-1):
            y, x = tmp[i]
            ny, nx = tmp[(i+r)%(len(tmp)-1)]

            ret[ny][nx] = li[y][x]
    return ret

li = rotate(li)
for i in range(n):
    print(*li[i])