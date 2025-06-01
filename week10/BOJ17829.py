n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def daq(n):
    global board

    if n == 2:
        return
    board_tmp = []
    for i in range(0, n, 2):
        row = []
        for j in range(0, n, 2):
            nums = []
            for a in range (2):
                for b in range(2):
                    nums.append(board[i+a][j+b])
            row.append(sorted(nums)[2])
        board_tmp.append(row)
    board = [arr[:] for arr in board_tmp]
    daq(n//2)

daq(n)
print(sorted(sum(board, []))[2])