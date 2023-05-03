#1157 - 단어 공부(Bronze 1)

word = input()
word_list = []
cnt = {}

for i in word:
    if not i.isupper():
        word_list.append(i.upper())
    else:
        word_list.append(i)

for i in word_list:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

result_list = sorted(cnt.items(), key=lambda x:-x[1])

flag = 0
max = result_list[0][1]
for i in result_list:
    if i[1] == max:
        flag += 1

if flag > 1:
    print('?')
else:
    print(result_list[0][0])