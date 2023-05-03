#2178 - 미로 탐색(silver 1)

from collections import deque
N, M = map(int, input().split(" "))

maze = []
for i in range(N):
    maze.append(list(map(int, input().rstrip())))

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

def bfs(x, y):

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < N and 0 <= next_y < M:
                if maze[next_x][next_y] == 1:
                    q.append((next_x, next_y))
                    maze[next_x][next_y] = maze[x][y] + 1

    return maze[N-1][M-1]

print(bfs(0, 0))
