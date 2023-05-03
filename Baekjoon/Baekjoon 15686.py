#15686 - 치킨 배달(Gold 5)

from itertools import combinations

def find_result(c):
    result = 0
    for h_loc in house:
        hx, hy = h_loc
        minimum = 10**9
        for c_loc in c:
            cx, cy = c_loc
            minimum = min(minimum, abs(hx - cx) + abs(hy - cy))
        result += minimum
    return result

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

c = combinations(chicken, m)
minimum = 10**9
for loc in c:
    minimum = min(minimum, find_result(loc))
print(minimum)