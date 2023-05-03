#6064 - 카잉 달력(silver 1)

import sys

T = int(input())

while T > 0:
    M, N, x, y = map(int, sys.stdin.readline().split())
    count = x
    result = False

    while count <= M * N:
        if (count - x) % M == 0 and (count - y) % N == 0:
            result = True
            break
        count += M

    if result:
        print(count)
    else:
        print(-1)

    T -= 1