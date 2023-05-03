#2448 - 별 찍기 11(Gold 4)

N = int(input())
n = N // 3
k = 0
while n > 1:
    k += 1
    n /= 2

tri = ["  *  ", " * * ", "*****"]

for _ in range(k):
    space = " " * len(tri)
    for i in range(len(tri)):
        tri.append(tri[i] + " " + tri[i])
        tri[i] = space + tri[i] + space

for i in tri:
    print(i)