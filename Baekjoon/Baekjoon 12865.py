#12856 - 평범한 배낭(Gold 5)

n, k = map(int, input().split())
dp = [0] * (k + 1)

for i in range(n):
    w, v = map(int, input().split())
    for weight in range(k, w - 1, -1):
        dp[weight] = max(dp[weight], dp[weight - w] + v)

print(dp[k])