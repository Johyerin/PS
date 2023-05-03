sen = input()
cnt = 1
for i in sen.rstrip():
    if i == ' ':
        cnt += 1

if sen[0] == ' ':
    cnt -= 1

if sen == ' ':
    print(0)
else:
    print(cnt)