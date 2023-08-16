# 계산기2 후위 표기법
# 입력된 문자열을 하나씩 보며 숫자가 들어온 경우 그대로 결과에 넣어주고
# 스택이 비어 있다면 연산자는 스택에 추가한다 스택이
# 스택이 비어있지 않다면 연산자도 출력해준다
# 연산자들의 우선순위를 정해서 스택에 저장한다
# 만약 스택 안에 있는 연산자가 새로 들어오는 연산자보다 우선 순위가 크다면
# 스택에 있는 연산자를 잠시 빼주고 우선 순위가 작은 연산자를 스택에 넣고
# 뺀 연산자를 다시 넣어준다.
# 문자열 반복이 종료된 후 스택을 확인하고 스택이 빌 때까지 결과에 출력한다.
# 후위 표기식 계산
# 스택에 숫자를 넣어서 연산자를 만날경우 꺼내어 순서에 맞게 계산한 후 다시 넣어준다
# 그 후 들어온 숫자와 원래 스택에 저장되어 있는 값을 다음 연산자에 맞추어 계산
# 연산이 끝난 후 마지막 스택에 있는 값이 최종 결과값
# 우선순위 해당 문제는 + 와 *만 존재하기 때문에 여러가지를 고려하지 않아도 됨
prio = {"+": 0, "*": 1}


def get_postfix(infix):
    stack = []
    postfix = ""
    for c in infix:
        if c not in list("+*"):
            postfix += c
        # 연산자일 경우
        else:
            # 빈스택이 아니고 스택안의 연산자의 우선순위가 크거나 같다면 전부 출력
            while stack and prio[stack[-1]] >= prio[c]:
                postfix += stack.pop()
            stack.append(c)
    while stack:
        postfix += stack.pop()
    return postfix


def get_result(postfix):
    stack = []
    for c in postfix:
        if c not in list("+*"):
            # 숫자로 추가해 주어야 계산 가능
            stack.append(int(c))
        # 연산자일 경우 스택 안에 요소가 2이상일 경우에 숫자를 2개 빼주어 연산자에 맞게 계산
        else:
            if len(stack) > 1:
                right = stack.pop()
                left = stack.pop()
                if c == "+":
                    result = left + right
                elif c == "*":
                    result = left * right
                stack.append(result)
    if stack:
        return stack.pop()


T = 10
for tc in range(1, T + 1):
    N = int(input())
    text = input()
    postfix = get_postfix(text)
    result = get_result(postfix)
    print(f"#{tc} {result}")
