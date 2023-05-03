#1991 - 트리 순회(Silver 1)

n = int(input())
tree = {}

def preOrder(root):
    print(root, end='')
    child = tree[root]

    if child[0] != '.':
        preOrder(child[0])

    if child[1] != '.':
        preOrder(child[1])

def inOrder(root):
    child = tree[root]

    if child[0] != '.':
        inOrder(child[0])

    print(root, end='')

    if child[1] != '.':
        inOrder(child[1])

def postOrder(root):
    child = tree[root]

    if child[0] != '.':
        postOrder(child[0])

    if child[1] != '.':
        postOrder(child[1])

    print(root, end='')

for _ in range(n):
    root, lchild, rchild = map(str, input().split())
    tree[root] = [lchild, rchild]

preOrder('A')
print('')
inOrder('A')
print('')
postOrder('A')