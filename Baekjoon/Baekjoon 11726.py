#11726 - 2xn 타일링(silver 3)

import sys

def find(n):
    tile = [0, 1, 2]
    for i in range(3, n + 1):
        tile.append(tile[i - 1] + tile[i - 2])
    return tile[n]

n = int(sys.stdin.readline())
print(find(n) % 10007)