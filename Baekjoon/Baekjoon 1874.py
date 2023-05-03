#1874 - 스택 수열(silver 2)

n = int(input())

list = []
for i in range(n):
    list.append(int(input()))

output = []
pointer = 0
check = False
for i in range(n):
    if list[i] > pointer:
        for j in range(list[i] - pointer):
            output.append("+")
        output.append("-")
        pointer = list[i]
    elif list[i] < pointer:
        if list[i] < list[i - 1]:
            output.append("-")
        else:
            check = True
if check:
    print("NO")
else:
    print(*output, sep="\n")