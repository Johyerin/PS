#7569 - 토마토(Gold 5)

import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
visit = [[[0] * m for _ in range(n)] for _ in range(h)]

result = 0
move_x = [-1, 1, 0, 0, 0, 0]
move_y = [0, 0, -1, 1, 0, 0]
move_z = [0, 0, 0, 0, -1, 1]

q = deque()

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            next_x = x + move_x[i]
            next_y = y + move_y[i]
            next_z = z + move_z[i]

            if next_x < 0 or next_x >= h or next_y < 0 or next_y >= n or next_z < 0 or next_z >= m:
                continue

            if graph[next_x][next_y][next_z] == 0 and visit[next_x][next_y][next_z] == 0:
                q.append((next_x, next_y, next_z))
                graph[next_x][next_y][next_z] = graph[x][y][z] + 1
                visit[next_x][next_y][next_z] = 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1 and visit[i][j][k] == 0:
                q.append((i, j, k))
                visit[i][j][k] = 1
bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))

print(result - 1)