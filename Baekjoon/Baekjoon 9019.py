#9019 - DSLR(Gold 4)

import sys
from collections import deque

def bfs(x, answer):
    q = deque()
    q.append(x)
    visited[x] = 1
    result = {x: ''}

    while(q):
        x = q.popleft()
        dslr = [(x * 2) % 10000, (x - 1) % 10000, (x % 1000) * 10 + (x // 1000), (x % 10) * 1000 + (x // 10)]

        for i in range(4):
            next_x = dslr[i]

            if visited[next_x] == 0:
                if i == 0:
                    result[next_x] = result[x] + 'D'
                elif i == 1:
                    result[next_x] = result[x] + 'S'
                elif i == 2:
                    result[next_x] = result[x] + 'L'
                else:
                    result[next_x] = result[x] + 'R'

                if next_x == answer:
                    return result[next_x]
                else:
                    q.append(next_x)
                    visited[next_x] = 1
                
t = int(sys.stdin.readline())
while t > 0:
    visited = [0] * 10000
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))
    t -= 1