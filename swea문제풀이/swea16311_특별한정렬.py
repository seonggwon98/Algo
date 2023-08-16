T = int(input())
# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())
    zero_arr = [[0] * N for _ in range(N)]
    count_ = 1
    zero_arr[0][0] = 1
    now_nr = 0
    now_nc = 0
    for i in range(N * N - 1):
        for d in range(4):
            nr = now_nr + dr[d]
            nc = now_nc + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if zero_arr[nr][nc] == 0:
                    now_nr = nr
                    now_nc = nc
                    count_ += 1
                    zero_arr[nr][nc] = count_
                    break

    print(f"#{tc}")
    for x in range(len(zero_arr)):  # 세로 크기
        for y in range(len(zero_arr[x])):  # 가로 크기
            print(zero_arr[x][y], end=' ')
        print()