#4949 - 균형잡힌 세상(silver 4)

while True:
    input_text = input()
    if input_text == '.':
        break
    stack = []
    cnt = True #yes를 출력하기 위한 조건 설정

    for i in input_text:
        if i == '(' or i == '[':
            stack.append(i) #스택에 push

        elif i == ')': #닫힌 괄호를 읽었을 때
            if len(stack) == 0: #스택 안이 비어있다면
                cnt = False #no를 출력하기 위한 조건 설정
                break #반복문 탈출
            if stack[-1] == '(': #스택의 마지막 원소가 알맞은 짝이라면
                stack.pop() #스택에서 pop(제거)
            else:
                cnt = False #아니라면 no 출력 조건

        elif i == ']':
            if len(stack) == 0:
                cnt = False
                break
            if stack[-1] == '[':
                stack.pop()
            else:
                cnt = False

    if cnt == True and not stack: #출력 조건이 True이고 스택이 비어있을 때(괄호가 모두 알맞은 짝이 있음)
        print('yes')
    else:
        print('no')