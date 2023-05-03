#1946 - 신입 사원(Silver 1)

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    people = []

    for _ in range(n):
        people.append(list(map(int, sys.stdin.readline().split())))
    people.sort()
    cnt = 1
    interview = people[0][1]

    for i in range(1, n):
        if people[i][1] < interview:
            interview = people[i][1]
            cnt += 1
    print(cnt)