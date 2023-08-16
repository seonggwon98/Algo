
T = 10
for tc in range(1, T + 1):
    # 첫줄에는 회문의 길이
    # 그 밑으로는 8*8의 글자판
    N = int(input())
    text = [list(input()) for _ in range(8)]
    # 길이가 1인 경우 글자판 하나하나가 다 회문
    answer = 0
    if N == 1:
        answer = 64
    # 나머지의 경우 행과 열을 순회 하면서 주어진 길이에 맞추어 회문을 찾는다
    # 회문을 찾은 경우 answer에 수를 1개 더해준다.
    for i in range(8):
        # 리스트의 인덱스를 벗어나지 않기 위해
        # 전체 글자판의 한줄의 크기에서 N을 빼주고 +1을 해주어야함
        for j in range(8 - N + 1):
            # 해당 길이의 글자를 행 우선 열 우선 각각 추출
            word_r = ""
            word_c = ""
            count_r = 0
            count_c = 0
            for k in range(N):
                word_r += text[i][j + k]
                word_c += text[j + k][i]
            # 두 단어가 회문인지 확인
            # 뒤집어도 똑같은지 확인하는 과정
            for p in range(N//2):
                if word_r[p] == word_r[N - p - 1]:
                    count_r += 1
                if word_c[p] == word_c[N - p - 1]:
                    count_c += 1
            if count_r == N // 2:
                answer += 1
            if count_c == N // 2:
                answer += 1
    print(f"#{tc} {answer}")




