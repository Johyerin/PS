#17070 - 파이프 옮기기 1(Gold 5)

n = int(input())
pipe = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    if pipe[0][i] == 0:
        dp[0][0][i] = 1

for i in range(1, n):
    for j in range(1, n):
        if pipe[i][j] == 0 and pipe[i - 1][j] == 0 and pipe[i][j - 1] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

        if pipe[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])