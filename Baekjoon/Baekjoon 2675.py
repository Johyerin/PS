t = int(input())
while(t > 0):
    r, s = map(str, input().split())
    for i in s:
        print(i * int(r), end= '')
    print()
    t -= 1