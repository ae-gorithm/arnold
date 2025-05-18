# 분할 정복
import sys
lines = sys.stdin.readlines()

# ---
# ---------
# ---------         ---------
# ---------         --------- / n=3

def daq(st, n, start, end):
    l = 3**n
    if n == 0:
        return
    
    st[start:end] = st[start:start + (l//3)] + [" "] * (((l//3)*2) - (l//3)) + st[start + (2*(l//3)):end]
    for i in range(0, l, 3**(n-1)):
        daq(st, n-1, start+i, start+i+(3**(n-1)))
    
    return st

for line in lines:
    n = int(line)
    if n == 0:
        print('-')
    else:
        st = "-" * 3**n
        print(''.join(daq(list(st), n, 0, 3**n)))