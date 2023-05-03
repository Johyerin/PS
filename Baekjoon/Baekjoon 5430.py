#5430 - AC(Gold 5)

import sys
from collections import deque

T = int(sys.stdin.readline())

while T > 0:
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    ary = sys.stdin.readline()
    error = 0
    rev = 0
    if n:
        q = deque(ary[1:-2].split(','))
    else:
        q = deque()

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if q:
                if rev % 2 == 0:
                    q.popleft()
                else:
                    q.pop()
            else:
                error = 1
                break
    if error:
        print('error')
    else:
        if rev % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
    T -= 1