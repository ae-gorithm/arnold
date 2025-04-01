import sys
n = int(input())
nums = list(map(int, input().split()))
pref = list(map(int, input().split()))
min_n = sys.maxsize
max_n = -sys.maxsize

def back(pref, ans, depth):
    global min_n
    global max_n
    next_ans = 0

    if depth == n:
        min_n = min(ans, min_n)
        max_n = max(ans, max_n)
        return
    
    for i in range(4):
        if pref[i] == 0:
            continue
        if i == 0:
            next_ans = ans + nums[depth]
        elif i == 1:
            next_ans = ans - nums[depth]
        elif i == 2:
            next_ans = ans * nums[depth]
        else:
            if ans < 0:
                next_ans = -(-ans // nums[depth])
            else:
                next_ans = ans // nums[depth]
        pref[i] -= 1
        back(pref, next_ans, depth+1)
        pref[i] += 1
        
back(pref, nums[0], 1)

print(max_n)
print(min_n)