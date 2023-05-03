#10816 - 숫자 카드2(silver 4)

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m_list:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")