#1967 - 트리의 지름(Gold 4)

import sys
sys.setrecursionlimit(10**9)

def dfs(start, weight, distance):
    for node, cost in tree[start]:
        if distance[node] == -1:
            distance[node] = cost + weight
            dfs(node, distance[node], distance)

n = int(input())
tree = [[] for _ in range(n + 1)]
distance_1 = [-1] * (n + 1)
distance_2 = [-1] * (n + 1)
distance_1[1] = 0

for _ in range(n - 1):
    parent, child, cost = map(int, input().split())
    tree[parent].append((child, cost))
    tree[child].append((parent, cost))

dfs(1, 0, distance_1)

index = 0
maxi = 0
for i in range(n + 1):
    if distance_1[i] > maxi:
        maxi = distance_1[i]
        index = i

distance_2[index] = 0
dfs(index, 0, distance_2)

print(max(distance_2))