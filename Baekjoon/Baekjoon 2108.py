#2108 - 통계학(silver 3)

import sys

n = int(sys.stdin.readline())
num_list = []

for i in range(n):
    num_list.append(int(sys.stdin.readline()))

sorted_num_list = sorted(num_list)

avg = round(sum(num_list)/n)
med = sorted_num_list[n//2]
rng = sorted_num_list[-1] - sorted_num_list[0]

dic = {}

for i in num_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

max_value = max(dic.values())
values = []
for key, value in dic.items():
 if value == max_value:
  values.append(key)

values = sorted(values)

if len(values) > 1:
    most = values[1]
else:
    most = values[0]

print(avg)
print(med)
print(most)
print(rng)