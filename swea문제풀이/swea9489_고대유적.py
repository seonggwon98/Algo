T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_long = 0
    for i in range(N):
        count_r = 0
        for j in range(M):
            if data[i][j] == 1:
                count_r += 1
                if max_long < count_r:
                    max_long = count_r
            else:
                count_r = 0

    for j in range(M):
        count_c = 0
        for i in range(N):
            if data[i][j] == 1:
                count_c += 1
                if max_long < count_c:
                    max_long = count_c
            else:
                count_c = 0
    print(f"#{tc} {max_long}")


