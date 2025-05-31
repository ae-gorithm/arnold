n = int(input())
postfix = input()
stack = []
value = []
for _ in range(n):
    value.append(int(input()))

for st in postfix:
    idx = ord(st)-65
    if 0 <= idx <= 25:
        stack.append(value[idx])
    else:
        a = stack.pop()
        b = stack.pop()
        oper = str(b) + st + str(a)
        stack.append(eval(oper))

print(f"{stack[0]:.2f}")