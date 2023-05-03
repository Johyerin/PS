#1654 - 랜선 자르기(silver 2)

k, n = map(int, input().split())
lan = []
for i in range(k):
    lan.append(int(input()))
min_len, max_len = 1, max(lan)

while min_len <= max_len:
    mid = (min_len + max_len) // 2
    line = 0
    for i in lan:
        line += i // mid

    if line >= n:
        min_len = mid + 1
    else:
        max_len = mid - 1
print(max_len)