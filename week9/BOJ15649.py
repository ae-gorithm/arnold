n, m = map(int, input().split())
li = []

def back(li):
    if len(li) == m:
        print(*li)
        li.pop()
        return
    
    for i in range(1, n+1):
        if i in li:
            continue
        li.append(i)
        back(li)
    if len(li) != 0:
        li.pop()

back(li)