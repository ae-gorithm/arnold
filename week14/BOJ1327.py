from collections import deque
n, k = map(int, input().split())
li = input().split()
s = set()
dq = deque([li])

ans = 0
flag = False
while dq:
    l = len(dq)
    for _ in range(l):
        nums = dq.popleft()
        numsToStr = ''.join(nums)
        if nums == list(map(str, range(1, n+1))):
            flag = True
            break
        if numsToStr in s:
            continue
        s.add(numsToStr)

        for i in range(n-k+1):
            tmp = nums.copy()
            tmp[i:i+k] = reversed(tmp[i:i+k])
            dq.append(tmp)
    if flag:
        break
    ans += 1

if not flag:
    print(-1)
else:
    print(ans)