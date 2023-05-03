#2667 - 단지 번호 붙이기(silver 1)

from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

move_x = [0, 0, -1, 1]
move_y = [-1, 1, 0, 0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if 0 <= next_x < N and 0 <= next_y < N:
                if graph[next_x][next_y] == 1:
                    graph[next_x][next_y] = 0
                    q.append((next_x, next_y))
                    count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(i, j))
result.sort()

print(len(result))
for i in result:
    print(i)