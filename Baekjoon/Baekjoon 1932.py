#1932 - 정수 삼각형(Silver 1)

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] += tri[i - 1][j]
        elif j == len(tri[i]) - 1:
            tri[i][j] += tri[i - 1][j - 1]
        else:
            tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])

print(max(tri[-1]))