b = str(bin(int(input())))

ans = 0
for i in b:
    if i == '1':
        ans += 1
print(ans)


# if x == 64:
#     print(1)
#     exit()
# wood = [64]
# while True:
#     n = wood.pop()
#     if sum(wood) + n/2 > x:
#         wood.append(n/2)
#     else:
#         wood.append(n/2)
#         if sum(wood)==x:
#             print(len(wood))
#             break
#         wood.append(n/2)