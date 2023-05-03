#10989 - 수 정렬(bronze 1)

import sys

n = int(sys.stdin.readline())
num_list = [0] * 10000

for i in range(n):
    num_list[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i + 1)