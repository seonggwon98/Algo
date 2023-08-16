dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flower = 0
    for i in range(N):
        for j in range(M):
            # 현재 위치를 (i,j)를 정했다
            sum_flower = 0
            for d in range(4):
                    ni = i + dr[d]
                    nj = j + dc[d]
                    if 0 <= ni < N and 0 <= nj < M:
                        sum_flower += arr[ni][nj]
            sum_flower += arr[i][j]
            if max_flower < sum_flower:
                max_flower = sum_flower
    print(f"#{tc} {max_flower}")