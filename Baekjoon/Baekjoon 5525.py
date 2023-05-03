#5525 - IOIOI(silver 1)

N = int(input())
M = int(input())
S = input()
count = 0

for i in range(M):
    if S[i] == 'I' and i < M:
        if S[i:i + 2 * N + 1] == 'I' + N * 'OI':
            count += 1

print(count)

#시간 초과 코드