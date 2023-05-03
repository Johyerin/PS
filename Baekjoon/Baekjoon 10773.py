#10773 - 제로(silver 4)

import sys

num = int(sys.stdin.readline())
stack = []

for i in range(num):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        stack.pop()
    else:
        stack.append(input_num)

print(sum(stack))