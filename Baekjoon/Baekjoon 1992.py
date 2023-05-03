#1992 - 쿼드트리(silver 1)

import sys
sys.setrecursionlimit(10**6)

def compression(ary):
    ary1 = []
    ary2 = []
    ary3 = []
    ary4 = []
    n = len(ary)
    m = len(ary) // 2

    check = ary[0][0]
    for i in range(n):
        for j in range(n):
            if check != ary[i][j]:
                check = -1
                break

    if check == -1:
        for i in range(n):
            if i < m:
                ary1.append(ary[i][0:m])
                ary2.append(ary[i][-m:])
            else:
                ary3.append(ary[i][0:m])
                ary4.append(ary[i][-m:])

        print('(', end='')
        compression(ary1)
        compression(ary2)
        compression(ary3)
        compression(ary4)
        print(')', end='')

    elif check == '1':
        print(1, end='')
    else:
        print(0, end='')

N=int(input())
array = []
for i in range(N):
    array.append(input())

compression(array)