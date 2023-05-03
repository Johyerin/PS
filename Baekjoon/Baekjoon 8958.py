#8958 - OX퀴즈(Bronze 2)

t = int(input())

for _ in range(t):
    ox = input()
    score = 0
    result = 0
    for i in ox:
        if i == "O":
            score += 1
        else:
            score = 0
        result += score
    print(result)