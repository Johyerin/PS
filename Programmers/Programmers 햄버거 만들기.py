'''def solution(ingredient):
    answer = 0
    stack = []

    for i in ingredient:
        if len(stack) >= 4 and i == 1:
            tmp_array = []
            flag = 1
            for j in range(3):
                tmp = stack.pop()
                tmp_array.append(tmp)
                if tmp == 3 - j:
                    continue
                else:
                    flag = 0
                    break

            if flag:
                answer += 1
                continue
            else:
                for _ in range(len(tmp_array)):
                    stack.append(tmp_array.pop())
                stack.append(i)
        else:
            stack.append(i)

    return answer'''

from collections import deque
def solution(ingredient):
    answer = 0
    ingredient_q = deque()
    hamburger_q = deque()

    for i in ingredient:
        ingredient_q.append(i)

        if len(ingredient_q) >= 4 and i == 1:
            for _ in range(4):
                hamburger_q.appendleft(ingredient_q.pop())

            if list(hamburger_q) == [1, 2, 3, 1]:
                hamburger_q.clear()
                answer += 1
            else:
                for _ in range(4):
                    ingredient_q.append(hamburger_q.popleft())

    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))