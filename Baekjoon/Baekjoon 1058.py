#1058 - 친구(Silver 2)

n = int(input())
array = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j != k and (array[j][k] == 'Y' or (array[j][i] == 'Y' and array[i][k] == 'Y')):
                visited[j][k] = 1

result = 0
for i in visited:
    result = max(result, sum(i))
print(result)