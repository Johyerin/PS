#16236 - 아기상어(Gold 3)

import sys
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    eat = []
    global shark
    visited = [[0] * n for _ in range(n)]

    move_x = [0, 0, -1, 1]
    move_y = [-1, 1, 0, 0]

    while q:
        x, y, dist = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1

                if 0 < space[next_x][next_y] < shark:
                    eat.append((next_x, next_y, dist + 1))
                elif space[next_x][next_y] == 0 or space[next_x][next_y] == shark:
                    q.append((next_x, next_y, dist + 1))

    if eat:
        eat.sort(key=lambda x:(x[2], (x[0], x[1])))
        return eat[0]
    else:
        return 0

n = int(sys.stdin.readline())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
shark = 2
eat_cnt = 0
result = 0

empty = True
for i in range(n):
    for j in range(n):
        if space[i][j] and space[i][j] != 9:
            empty = False
        elif space[i][j] == 9:
            space[i][j] = 0
            pos_x, pos_y = i, j

if empty:
    print(0)
else:
    while True:
        if eat_cnt == shark:
            shark += 1
            eat_cnt = 0

        fish = bfs(pos_x, pos_y)
        if fish:
            x, y, dist = fish
            space[x][y] = 0
            eat_cnt += 1
            result += dist
            pos_x, pos_y = x, y
        else:
            break
    print(result)