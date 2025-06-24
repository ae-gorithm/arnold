import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    oper = list(input().strip())
    n = int(input())
    if n == 0:
        dq = []
        input()
    else:
        dq = deque(input()[1:-2].split(','))
    
    func = [0, 'dq.popleft()', 'dq.pop()']
    operIdx = 1

    for o in oper:
        if o == 'R':
            operIdx *= -1
        else:
            if len(dq) == 0:
                print('error')
                break
            eval(func[operIdx])
    else:
        if operIdx == -1:
            dq.reverse()
        print('[', end='')
        print(','.join(dq), end='')
        print(']')
        