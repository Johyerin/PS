#5639 - 이진 검색 트리(Gold 5)

import sys
sys.setrecursionlimit(10 ** 5)

def post(start, end, tree):
    if start == end:
        return []

    if end - start <= 1:
        return [tree[start]]

    root = tree[start]
    divide = end
    for i in range(start + 1, end):
        if tree[i] > root:
            divide = i
            break

    left_tree = post(start + 1, divide, tree)
    right_tree = post(divide, end, tree)

    result_tree =  left_tree + right_tree + [root]

    return result_tree

tree = []
num = sys.stdin.readline().rstrip()
while True:
    if num == '':
        break
    else:
        tree.append(int(num))
    num = sys.stdin.readline().rstrip()

result_tree = post(0, len(tree), tree)
for i in result_tree:
    print(i)