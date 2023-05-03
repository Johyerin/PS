sum = 0
for i in input().rstrip():
    if i != ' ':
        sum += int(i) ** 2

print(sum % 10)