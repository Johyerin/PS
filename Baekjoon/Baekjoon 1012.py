#1012 - 유기농 배추(silver 2)

import sys
sys.setrecursionlimit(10000)

def find(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return

    if array[x][y] == 1:
        array[x][y] = 0
        find(x + 1, y)
        find(x, y + 1)
        find(x - 1, y)
        find(x, y - 1)
    else:
        return

    array[x][y] = 0
    find(x + 1, y)
    find(x, y + 1)
    find(x - 1, y)
    find(x, y - 1)

case_num = int(sys.stdin.readline())
while case_num > 0:
    m, n, k = map(int, (sys.stdin.readline().split()))
    array = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, (sys.stdin.readline().split()))
        array[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                find(i, j)
                count += 1

    print(count)
    case_num -= 1