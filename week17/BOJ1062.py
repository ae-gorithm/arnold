n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()

words = []
for i in range(n):
    s = input().strip()[4:-4]
    words.append(set(s))

selected = [False for _ in range(26)]

for ch in 'antic':
    selected[ord(ch) - ord('a')] = True

ans = 0
def back(num, start):
    global ans

    if num == k:
        ret = 0
        for word in words:
            for ch in word:
                if not selected[ord(ch) - ord('a')]:
                    break
            else:
                ret += 1
        ans = max(ans, ret)
        return
    
    for i in range(start, 26):
        if selected[i]: continue
        selected[i] = True
        back(num+1, i+1)
        selected[i] = False

back(5, 0)
print(ans)