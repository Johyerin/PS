#9935 - 문자열 폭발(Gold 4)

string = input()
bomb = input()

string_stack = []
bomb_stack = [i for i in bomb]

for i in string:
    string_stack.append(i)

    if len(string_stack) >= len(bomb) and i == bomb[-1]:
        tmp_string = ''
        flag = 0
        for _ in range(len(bomb)):
            tmp = string_stack.pop()
            tmp_string += tmp
            if tmp == bomb_stack.pop():
                continue
            else:
                flag = 1
                break
        if flag:
            for j in range(1, len(tmp_string) + 1):
                string_stack.append(tmp_string[-j])
        bomb_stack = [i for i in bomb]

if string_stack == []:
    print("FRULA")
else:
    for i in string_stack:
        print(i, end='')

