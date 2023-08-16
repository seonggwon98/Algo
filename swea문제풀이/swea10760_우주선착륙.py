T = int(input())
# 0 : 상 1 : 우상 2 : 우 3 : 우하 4 : 하 5 : 좌하 6 : 좌 7 : 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    height = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            ssafy_1 = height[i][j]
            count = 0
            for n in range(8):
                nr = i + dr[n]
                nc = j + dc[n]
                if 0 <= nr < N and 0 <= nc < M:
                    if ssafy_1 > height[nr][nc]:
                        count += 1
                        if count > 3:
                            result += 1
                            break
    print(f"#{tc} {result}")
