def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M


N, M = map(int, input().split())
ground = [input() for _ in range(N)]
# 해당 칸이 육지 일 때 6방향을 보면서 물이라면 해변의 길이에 추가해 준다.
# 0 : 상 1 : 하 2 : 좌 3 : 우 4 : 우상 5 : 좌상 6 : 우하 7 : 좌하
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]
beach = 0
for i in range(N):
    for j in range(M):
        if ground[i][j] == "#":
            if i % 2 == 0:
                for n in range(8):
                    if n != 4 and n != 6:
                        nr = i + dr[n]
                        nc = j + dc[n]
                        if is_valid(nr, nc) and ground[nr][nc] == ".":
                            beach += 1
            else:
                for n in range(8):
                    if n != 5 and n != 7:
                        nr = i + dr[n]
                        nc = j + dc[n]
                        if is_valid(nr, nc) and ground[nr][nc] == ".":
                            beach += 1
print(beach)
