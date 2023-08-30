def find_min(r, c, now_sum):
    global min_i
    # 종료 조건 r,c의 위치가 N-1이라면 종료
    if r == N - 1 and c == N - 1:  # (r,c) == (N-1,N-1)
        if min_i > now_sum:
            min_i = now_sum
        return
    for n in range(2):
        nr = r + dr[n]
        nc = c + dc[n]
        if 0 <= nr < N and 0 <= nc < N:
            find_min(nr, nc, now_sum + arr[nr][nc])
    #         # 해당 칸으로 이동해서 다음을 진행하고
    #         min_i += arr[nr][nc]
    #         find_min(nr, nc)
    #         # 전에 있던 칸으로 돌아와 진행해야하기 때문에 더해준 값 다시 빼준다.
    #         min_i -= arr[nr][nc]


dr = [0, 1]
dc = [1, 0]
T = int(input())
for tc in range(1, T + 1):
    # N : 가로 세로 칸 수
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    r = c = 0
    min_i = 1000000
    find_min(r, c, arr[r][c])
    print(f"#{tc} {min_i}")
