T = int(input())

for tc in range(1, T + 1):
    text = input()
    N = len(text)
    answer = 0
    start = 0
    end = N - 1
    # 한 반복은 처음부터 중간 까지 한 반복은 끝부터 중간 까지 진행 시켜서 값들이 같은지 확인
    # 한개라도 다른 값이 있다면 회문이 아님
    while start <= end:
        if text[start] == text[end]:
            start += 1
            end -= 1
            if start > N // 2 or end < N // 2:
                answer = 1
                break
        else:
            answer = 0
            break
    print(f"#{tc} {answer}")

