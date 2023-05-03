result = []
for _ in range(10):
    num = int(input())
    rest = num % 42
    if rest in result:
        continue
    else:
        result.append(rest)
print(len(result))