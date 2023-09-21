from heapq import heappush, heappop


def dijkstra(sr, sc):
    heap = []
    # 현재 위치에서 연료량 0으로 변경
    fuel[sr][sc] = 0
    # heap에 연료량과 시작점을 넣어준다.
    heappush(heap, (0, sr, sc))
    # 4방향을 이동할 수 있음
    while heap:
        w, r, c = heappop(heap)
        if fuel[r][c] < w:
            continue
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            height_diff = 0
            if 0 <= nr < N and 0 <= nc < N:
                if map_h[r][c] < map_h[nr][nc]:
                    height_diff = map_h[nr][nc] - map_h[r][c]
                cost = fuel[r][c] + height_diff + 1
                # 새로 계산한 연료량 이전보다 작으면 갱신
                if cost < fuel[nr][nc]:
                    fuel[nr][nc] = cost
                    # 갱신 될때만 추가 해준다.
                    heappush(heap, (cost, nr, nc))


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T + 1):
    # N : 가로 세로의 칸수
    N = int(input())
    map_h = [list(map(int, input().split())) for _ in range(N)]
    # 누적 해당 위치까지 연료량 저장
    INF = int(1e9)
    fuel = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)
    print(f"#{tc} {fuel[N-1][N-1]}")
