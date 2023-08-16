T = int(input())
for tc in range(1, T + 1):
    text = list(input())
    # 스택을 활용해서 괄호를 검사를 진행한다.
    # 열린 괄호의 경우 스택에 넣어주고 닫힌 괄호를 만났을 때 해당 괄호와 짝이 맞는다면
    # 스택에서 빼준다. 짝이 맞지 않는다면 오류
    # 빈 스택에서 더 빼야될 경우도 오류
    # 마지막에 빈 스택이 아니어도 오류
    # 오류가 발견될 경우 0 정상일 경우 1출력
    stack = []
    answer = 1
    for i in text:
        if i == "(" or i == "{":
            stack.append(i)
            continue
        if i == ")" or i == "}":
            if stack:
                check = stack.pop()
                if not(check == "(" and i == ")" or check == "{" and i == "}"):
                    answer = 0
                    break
            else:
                answer = 0
                break
    if stack:
        answer = 0
    print(f"#{tc} {answer}")