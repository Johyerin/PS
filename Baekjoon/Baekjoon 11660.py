#11660 - 구간 합 구하기 5(Silver 1)

import sys

n, m = map(int, sys.stdin.readline().split())
table = [[0] for _ in range(n + 1)]

for i in range(1, n + 1):
    table[0].append(0)
    for num in sys.stdin.readline().split():
        table[i].append(int(num))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        table[i][j] += table[i - 1][j] + table[i][j - 1] - table[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(table[x2][y2] - table[x2][y1 - 1] - table[x1 - 1][y2] + table[x1 - 1][y1 - 1])