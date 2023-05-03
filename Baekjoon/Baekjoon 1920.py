#1920 - 수 찾기(silver 4)

import sys

N = int(sys.stdin.readline())
num_list = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())
input_list = list(sys.stdin.readline().split())

for i in input_list:
    if i in num_list:
        print(1)
    else:
        print(0)