#11047 - 동전(Silver 4)

N, K = map(int, input().split())
coin = []

for i in range(N):
    coin.append(int(input()))

result = 0
for i in reversed(range(N)):
    result += K // coin[i]
    K = K % coin[i]

print(result)