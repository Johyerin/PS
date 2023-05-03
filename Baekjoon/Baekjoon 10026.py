#10026 - 적록색약(Gold 5)

from collections import deque

N = int(input())
rgb = [list(input().strip()) for _ in range(N)]

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < N and 0 <= next_y < N and rgb[next_x][next_y] == rgb[x][y] and visit[next_x][next_y] == 0:
                visit[next_x][next_y] = 1
                q.append((next_x, next_y))

def counting():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                bfs(i, j)
                cnt += 1
    return cnt

visit = [[0] * N for _ in range(N)]
print(counting(), end = ' ')

visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'
print(counting())