#14500 - 테트로미노(Gold 4)

import sys

def FindWithDfs(x, y, cnt, sum):
    global result
    if cnt == 3:
        result = max(sum, result)
    else:
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < n and 0 <= next_y < m and visited[next_x][next_y] == 0:
                visited[next_x][next_y] = 1
                FindWithDfs(next_x, next_y, cnt + 1, sum + paper[next_x][next_y])
                visited[next_x][next_y] = 0

def FindWithDirection(x, y, sum):
    global result
    cnt = 0

    for i in range(4):
        next_x = x + move_x[i]
        next_y = y + move_y[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            sum += paper[next_x][next_y]
            cnt += 1

    if cnt == 3:
        result = max(sum, result)

    if cnt == 4:
        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            sum -= paper[next_x][next_y]
            result = max(sum, result)
            sum += paper[next_x][next_y]

n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]
result = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        FindWithDfs(i, j, 0, paper[i][j])
        FindWithDirection(i, j, paper[i][j])
        visited[i][j] = 0
print(result)