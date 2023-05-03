#1931 - 회의실 배정(silver 1)

N = int(input())
meeting = []
cnt = 1

for i in range(N):
    a, b = map(int, input().split())
    meeting.append([a, b])

meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

start, end = meeting[0][0], meeting[0][1]
for i in range(1, N):
    if end <= meeting[i][0]:
        start, end = meeting[i][0], meeting[i][1]
        cnt += 1

print(cnt)