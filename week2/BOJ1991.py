import sys
input = sys.stdin.readline

n = int(input())
tree = [[-1, -1] for _ in range(n)]

for _ in range(n):
    a, b, c = input().split()
    a = ord(a) - 65
    b = ord(b) - 65
    c = ord(c) - 65
    if b != -19:
        tree[a][0] = b
    if c != -19:
        tree[a][1] = c

def preOrder(node):
    if node >= n or node == -1:
        return
    print(chr(node+65), end="")
    preOrder(tree[node][0])
    preOrder(tree[node][1])

def inOrder(node):
    if node >= n or node == -1:
        return
    inOrder(tree[node][0])
    print(chr(node+65), end="")
    inOrder(tree[node][1])

def postOrder(node):
    if node >= n or node == -1:
        return
    postOrder(tree[node][0])
    postOrder(tree[node][1])
    print(chr(node+65), end="")

preOrder(0)
print()
inOrder(0) 
print()   
postOrder(0)
print()
