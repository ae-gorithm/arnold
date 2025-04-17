import sys
sys.setrecursionlimit(10000)
str1 = input()
str2 = input()
ans = ""
#   A C A Y K P
# C 0 1 1 1 1 1
# A 1 1 2 2 2 2
# P 1 1 2 2 2 3
# C 1 2 2 2 2 3
# A 1 2 3 3 3 3
# K 1 2 3 3 4 4

def lcs(i ,j):
    global ans
    if i == 0 or j == 0:
        return
    
    if str1[j-1] == str2[i-1]:
        lcs(i-1, j-1)
        ans += str1[j-1]
    elif dp[i][j-1] > dp[i-1][j]:
        lcs(i, j-1)
    else:
        lcs(i-1, j)

dp = [[0 for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]

for i in range(1, len(str2)+1):
    for j in range(1, len(str1)+1):
        if str1[j-1] == str2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs(len(str2), len(str1))
print(dp[len(str2)][len(str1)])
print(ans)