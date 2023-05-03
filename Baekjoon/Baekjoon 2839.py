n = int(input())
dp = [-1] * 5001

for i in range(n + 1):
    if dp[i - 3] > 0 and dp[i - 5] > 0:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

    else:
        if i % 3 == 0:
            dp[i] = dp[i - 3] + 1
        elif i % 5 == 0:
            dp[i] = dp[i - 5] + 1
print(dp[n])