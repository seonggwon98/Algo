# 상 우상 우 우하 하 좌하 좌 좌상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
T = int(input())
for tc in range(1, T + 1):
    # N : 보드 한 변의 길이  M : 돌을 놓는
    N, M = map(int, input().split())
    # M줄 동안 돌 놓는 위치와 색 주어짐
    b = 1
    w = 2
    info = [list(map(int, input().split())) for _ in range(M)]
    # 제일 먼저 N * N의 배열을 만들고 그 중앙 4칸에
    # WBBW순으로 칸을 채운 후 게임 시작
    # 보드의 첫 시작은 1부터 시작 하므로 행열을 각각 1 개씩 더 만들어 준다
    board = [[0] * N + 1 for _ in range(N + 1)]
    middle = N // 2
    board[middle][middle] = w, board[middle][middle + 1] = b
    board[middle + 1][middle] = b, board[middle + 1][middle + 1]
    for i in range(M):
        r = info[i][0], c = info[i][1], color = info[i][2]
        board[r][c] = color
        for j in range(8):
            for n in range(N):
                nr = r + dr[j] * n
                nc = c = dc[j] * n
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == color:
                        break

