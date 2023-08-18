def start_point(n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                sti, stj = i, j
                return sti, stj


def is_value(nr, nc):
    return 0 <= nr < N and 0 <= nc < N


def maze_game(sti, stj, n):  # sti, stj : 시작 정점 행, 열 n : 미로의 크기
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sti, stj))  # 시작 정점 q에 저장
    visited[sti][stj] = 1  # 시작 정점 방문 처리
    while q:  # 빈 queue가 아닐경우 계속 진행
        r, c = q.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_value(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                if maze[nr][nc] == 3:
                    return visited[r][c]-1
                    break
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
    return 0



dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    # N : 미로의 크기
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    sti, stj = start_point(N)
    result = maze_game(sti, stj, N)
    print(f"#{tc} {result}")