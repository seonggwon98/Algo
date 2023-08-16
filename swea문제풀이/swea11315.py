T = int(input())
for tc in range(1, T + 1):
    # 오목 문제
    # 첫 줄은 N * N 배열
    # 5개 이상 연속하여 돌이 존재하는지 체크하는 문제
    # 가로와 세로 그리고 대각선 체크
    # 작은 대각선들도 체크 해주어야한다.
    N = int(input())
    # N 번만큼 반복해서 오목판의 배열을 받아 준다.
    arr = [list(input()) for _ in range(N)]
    answer = "NO"
    for i in range(N):
        count_r = 0
        count_c = 0
        for j in range(N):
            # 역방향 대각선을 확인한다.
            # 대각선 확인 출발 위치는 0행 이거나 끝 열 일때 확인 시작
            # 행은 증가 열은 감소 시키면서 해당 위치의 값을 확인
            # 돌의 카운트가 5개 이상이라면 YES
            if i == 0 or j == N - 1:
                r, c = i, j
                c_r_d = 0
                while r < j + 1:
                    if arr[r][c] == 'o':
                        c_r_d += 1
                    else:
                        c_r_d = 0
                    r += 1
                    c -= 1
                    if c_r_d > 4:
                        answer = 'YES'
                        break
            # 순방향 대각선을 확인 하는 구문
            # 시작 위치는 0행과 0열의 위치에 있을 경우 시작
            # 해당 위치에서 행 과 열이 모두 1씩 증가하며 대각선 요소들을 확인
            # 연속적으로 돌이 5개 이상일 때 YES
            if i == 0 or j == 0:
                count_diagonal = 0
                r, c = i, j
                while r < N and c < N:
                    if arr[r][c] == 'o':
                        count_diagonal += 1
                    else:
                        count_diagonal = 0
                    r += 1
                    c += 1
                    if count_diagonal > 4:
                        answer = "YES"
                        break
            # 행 우선 순회 열 우선 순회를 각각 진행하여 카운트 5 이상 일때 YES
            # YES 반복 종료
            if arr[i][j] == 'o':
                count_r += 1
            else:
                count_r = 0
            if arr[j][i] == 'o':
                count_c += 1
            else:
                count_c = 0
            if count_r > 4 or count_c > 4:
                answer = "YES"
                break
        # YES 배열 탐색 정지
        if answer == "YES":
            break
    print(f"#{tc} {answer}")
