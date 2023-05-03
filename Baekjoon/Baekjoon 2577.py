a = int(input())
b = int(input())
c = int(input())

numbers = [0] * 10

result = str(a * b * c)

for i in result:
    numbers[int(i)] += 1

for i in numbers:
    print(i)