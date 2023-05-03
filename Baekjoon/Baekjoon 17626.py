#17626 - Four Squares(silver 3)

import sys

N = int(sys.stdin.readline())
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    minimum = 4
    for j in range(1, int(i ** 0.5) + 1):
        minimum = min(minimum, dp[i - (j ** 2)])
    dp[i] = minimum + 1

print(dp[N])