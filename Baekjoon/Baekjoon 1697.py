#1697 - 숨바꼭질(silver 1)

from collections import deque

n, k = map(int, input().split())
MAX = 200000
sec = [0] * MAX

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        next = [x - 1, x + 1, x * 2]

        if x == k:
            print(sec[k])
            return

        if abs(k - x) > abs(k - x * 2) and sec[x * 2] == 0:
            q.append(x * 2)
            sec[x * 2] = sec[x] + 1

        for i in next:
            if i >= 0 and i < MAX and sec[i] == 0:
                q.append(i)
                sec[i] = sec[x] + 1

bfs(n, k)