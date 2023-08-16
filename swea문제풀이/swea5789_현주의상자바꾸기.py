T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    # Q 개의 줄에 i번째 줄의 LR 저장
    LR = [list(map(int, input().split())) for _ in range(Q)]
    # 처음 비워져 있는 0 배열
    N_arr = [0]*(N+1)
    # i 는 1부터 Q + 1 까지 값
    for i in range(1, Q+1):
        L, R = LR[i-1]
        for j in range(L, R+1):
            N_arr[j] = i

    print(f"#{tc}", *N_arr[1 : N+1])

