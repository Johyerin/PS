#2579 - 계단 오르기(silver 3)

import sys

n = int(sys.stdin.readline())
stairs = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    stairs[i] = int(sys.stdin.readline())

for i in range(3, n + 1):
    dp[i] = (max(dp[i - 3] + stairs[i - 1], dp[i - 2]) + stairs[i])

print(dp[n])