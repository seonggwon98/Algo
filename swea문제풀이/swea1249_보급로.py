from heapq import heappop, heappush


def restore(sr, sc):
    # 처음 위치 초기화 해줌
    heap = []
    heappush(heap, (0, sr, sc))
    distance[sr][sc] = 0
    while heap:
        # 걸리는 시간과 위치 힙에 넣어줌
        t, r, c = heappop(heap)
        # 해당 위치의 최단 경로 값이 계산 중인 값보다 작다면 pass
        if distance[r][c] < t:
            continue
        # 2차원 배열 4방향 델타 탐색 통해서 다음 위치 찾고
        # 다음 위치의 최단 경로 값과 계산한 값 비교 후 더 작다면 갱신해준다.
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                nd = distance[r][c] + road[nr][nc]
                if distance[nr][nc] > nd:
                    distance[nr][nc] = nd
                    heappush(heap, (nd, nr, nc))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input())) for _ in range(N)]
    distance = [[1000000000] * N for _ in range(N)]
    restore(0,0)
    print(f"#{tc} {distance[N-1][N-1]}")
