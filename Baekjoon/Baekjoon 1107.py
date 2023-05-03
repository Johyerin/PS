#1107 - 리모컨(Gold 5)

import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())
error_btn = list(sys.stdin.readline().split())

res = abs(100 - n)

for num in range(1000000):
    tmp = str(num)
    for i in range(len(tmp)):
        if tmp[i] in error_btn:
            break
    else:
        res = min(res, len(tmp) + abs(num - n))

print(res)