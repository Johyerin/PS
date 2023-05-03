#성격 유형 검사하기(Lv.1)

def solution(survey, choices):
    type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for s, c in zip(survey, choices):
        if 1 <= c <= 3:
            type[s[0]] += 4 - c
        elif 5 <= c <= 7:
            type[s[1]] += c - 4

    answer = ''
    answer += add_answer("R", "T", type)
    answer += add_answer("C", "F", type)
    answer += add_answer("J", "M", type)
    answer += add_answer("A", "N", type)

    return answer

def add_answer(a, b, type):
    if type[a] >= type[b]:
        return a
    else:
        return b

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

print(solution(survey, choices))