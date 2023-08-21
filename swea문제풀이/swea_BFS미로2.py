def start_point(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j


def is_value(nr, nc):
    return 0 <= nr < N and 0 <= nc < N


def maze_game(start, n):
    sti, stj = start
    # 방문 확인용 배열 그리고 queue 준비
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sti, stj))
    # 시작 점 방문 처리
    visited[sti][stj] = 1
    while q:
        r, c = q.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if maze[nr][nc] == 3:
                return 1
            if is_value(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 0


# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = 10
for t in range(1, T + 1):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(100)]
    print(f"#{tc}", end=" ")
    print(maze_game(start_point(100), 100))
