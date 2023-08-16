T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    for i in range(len(text)):
        stack.append(text[i])
        if len(stack) >= 2:
            if stack[len(stack)-1] == stack[len(stack)-2]:
                for j in range(2):
                    stack.pop()

    print(f"#{tc} {len(stack)}")