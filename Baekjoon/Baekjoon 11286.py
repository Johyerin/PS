#11268 - 절댓값 힙(silver 1)

import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            num, sign = heappop(heap)
            print(int(num * sign))
        else:
            print(0)
    else:
        heappush(heap, [abs(x), x/abs(x)])