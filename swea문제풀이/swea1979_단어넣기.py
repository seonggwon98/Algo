T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    # 연속된 1의 수가 3개 일때 갯수를 증가
    # 행과 열 순회 각각 진행 해주어야 한다.
    total = 0
    for i in range(N):
        i_count = 0
        j_count = 0
        for j in range(N):
            # 먼저 해당 칸이 1인지 확인 후 1이라면 각각 카운트에서 카운트 해준다.
            # 카운트를 세어가다 해당 칸이 0이라면 해당 칸 전까지의 카운트를 확인하고 K라면 증가 그 후 카운트를 초기화
            if arr[i][j] == 1:
                i_count += 1
            else:
                if i_count == K:
                    total += 1
                i_count = 0

            if arr[j][i]:
                j_count += 1
            else:
                if j_count == K:
                    total += 1
                j_count = 0
        # 끝 칸에서 K길이가 될 수 도 있으니까 한번 확인후 더해준다
        if i_count == K:
            total += 1
        if j_count == K:
            total += 1
    print(f"#{tc} {total}")

