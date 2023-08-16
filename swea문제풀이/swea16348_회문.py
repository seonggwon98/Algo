T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    N_arr = [list(input()) for _ in range(N)]
    # 일단 행 우선 순회를 진행하여 회문을 찾는다
    # 주어진 길이에 맞추어 단어를 뽑아 낸 후 회문 여부를 파악한다.
    answer = ''
    for i in range(N):
        for j in range(N - M + 1):  # range 의 범위가 ~이상 ~미만 이기에 +1을 해주어 단어의 시작 지점 이동
            # 단어를 추출
            word_r = ""
            word_c = ""
            # 단어의 길이는 M개 이니까 M번 반복하고 해당 열의 값은 j + k가 된다
            for k in range(M):
                word_r += N_arr[i][j + k]
                word_c += N_arr[j + k][i]
            # 단어가 회문인지 확인
            count_r = 0
            count_c = 0
            for p in range(M // 2):
                if word_r[p] == word_r[M-p-1]:
                    count_r += 1
                if word_c[p] == word_c[M-p-1]:
                    count_c += 1
            if count_r == M // 2:
                answer = word_r
            if count_c == M // 2:
                answer = word_c
    print(f"#{tc} {answer}")