from collections import defaultdict

dic = defaultdict(int)
s = input()
n = len(s)

for i in range(n):
    for j in range(n-i):

        dic[s[j:j+i+1]] = 1

print(len(dic.keys()))
# s[0:0]
# s[1:1]
# s[2:2]
# s[3:3]
# s[4:4]

# s[0:1]
# s[1:2]
# s[2:3]
# s[3:4]

# s[0:2]
# s[1:3]
# s[2:4]

# s[0:3]
# s[1:4]

# s[0:4]