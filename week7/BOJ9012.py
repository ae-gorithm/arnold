import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stack = []
    s = input().rstrip()
    for ch in s:
        if ch == '(':
            stack.append(0)
        else:
            if len(stack) == 0:
                print("NO")
                break
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")