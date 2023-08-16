for t in range(10):    # 정답을 알고 있으므로 밑에서 위로 올라가는 방법으로 진행
    tc = int(input()) # 테스트 케이스 번호가 주어진다
    # 입력으로 100*100 배열을 받아 준다
    ladder_arr = [list(map(int, input().split())) for _ in range(100)]
    # 우선적으로 어떤 방향을 탐색할지 델타 배열을 통해 정해준다. 우 좌 상
    # 상
    dr = [0, 0, -1]
    dc = [1, -1, 0]
    N = len(ladder_arr)
    # 행의 인덱스가 0이 된다면 반복을 종료 while문을 쓰는 것이 좋을 것 같다.
    # 먼저 정답이 있는 인덱스의 정보를 저장해 출발 지점으로 삼는다
    # 델타 탐색을 통해  좌 우 상 순으로 탐색하며 지나간 위치는 0으로 바꾸어 준다(좌 우의 경우 다시 가는 경우가 생기므로)
    for i in range(N):
        if ladder_arr[99][i] == 2:
            now_r, now_c = 99, i
    while now_r > 0:
        for d in range(3):
            nr = now_r + dr[d]
            nc = now_c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if ladder_arr[nr][nc] == 1:
                    now_r, now_c = nr, nc
                    ladder_arr[nr][nc] = 0
        if now_r == 0:
            result = now_c

    print(f"#{tc} {result}")
