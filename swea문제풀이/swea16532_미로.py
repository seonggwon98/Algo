T = int(input())
# 0 : 상 1 : 하 2 : 우 3 : 좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    stack = []
    # 시작 포인트를 찾는다
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr, sc = i, j
    # 해당 포인트에서 델타 배열을 활용하여 이동이 가능한 칸의 방향으로 진행 한다.
    # 벽은 1 갈 수 있는 통로는 0 도착지점은 3
    # 도착 지점을 찾거나 더 이상 움직일 수 없는 경우 반복 종료
    answer = 0
    maze[sr][sc] = 1
    while not(answer):
        for n in range(4):
            nr = sr + dr[n]
            nc = sc + dc[n]
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
                if maze[nr][nc] == 0:
                    # 움직인 해당 칸을 1로 채워준다
                    stack.append((sr, sc))
                    maze[nr][nc] = 1
                    sr, sc = nr, nc
                    break
                if maze[nr][nc] == 3:
                    answer = 1
                    break
        # for문이 break에 의해 종료가 된 경우가 아닌경우
        # 4방향 중 이동 할 수 있는 곳이 없다는 뜻
        # 고로 전의 칸으로 돌아가면서 갈림길이 있는 칸 까지 가서 다시 진행
        else:
            if stack:
                sr, sc = stack.pop()
            else:
                break

    print(f"#{tc} {answer}")
