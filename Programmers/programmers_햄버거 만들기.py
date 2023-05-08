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