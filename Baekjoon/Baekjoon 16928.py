#16928 - 뱀과 사다리 게임(Gold 5)

from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    dice = [1, 2, 3, 4, 5, 6]

    while(q):
        x = q.popleft()

        for i in range(6):
            next_x = x + dice[i]

            if 0 < next_x <= 100 and visited[next_x] == 0:
                if next_x in ladder:
                    next_x = ladder[next_x]

                if next_x in snake:
                    next_x = snake[next_x]

                if visited[next_x] == 0:
                    q.append(next_x)
                    visited[next_x] = 1
                    cnt[next_x] = cnt[x] + 1


n, m = map(int, input().split())
ladder = {}
snake = {}

for _ in range(n):
    k, v = map(int, input().split())
    ladder[k] = v

for _ in range(m):
    k, v = map(int, input().split())
    snake[k] = v

cnt = [0] * 101
visited = [0] * 101

bfs(1)
print(cnt[100])