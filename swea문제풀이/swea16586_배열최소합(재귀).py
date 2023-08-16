def min_sum(i, N, s):
    global min_v
    # i행을 돌면서 j열을 선택
    # 다음 행은 선택한 j열을 제외한 나머지 열을 선택해야한다
    # 최적화 조건
    # 최솟값보다 진행중인 합이 더 클 경우
    if min_v < s:
        return
    # 종료 조건
    # i가 N과 같아졌을 때까지 진행

    if i == N:
        if min_v > s:
            min_v = s
        return
    # 재귀 호출
    else:
        for j in range(N):
            if not (select[j]):
                select[j] = 1
                min_sum(i + 1, N, s + numbers[i][j])
                select[j] = 0


T = int(input())
for tc in range(1, T + 1):
    # N개의 정수가 N줄에 걸쳐서 입력
    N = int(input())
    select = [0] * N
    numbers = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100
    now_sum = 0
    min_sum(0, N, now_sum)
    print(f"#{tc} {min_v}")
