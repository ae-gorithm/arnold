n, s = map(int, input().split())
nums = list(map(int, input().split()))
sumN = 0
cnt = 0
if sumN == s:
    cnt -= 1

def back(idx, ans):
    global sumN
    global cnt

    if ans == s:
        cnt += 1

    if idx == n:
        return

    for i in range(idx, n):
        sumN += nums[i]
        back(i+1, sumN)
        sumN -= nums[i]

back(0, 0)
print(cnt)