T = int(input())
for tc in range(1, T + 1):
    # 농장의 크기 : N*N
    N = int(input())
    price = [list(map(int, input())) for _ in range(N)]
    center = N // 2
    sr, sc = center, center
    # 배열 전체를 돌면서 중심에서의 길이가 N // 2 이하인 부분들의 위치의 값을 더해주면 된다.
    total = 0
    for i in range(N):
        for j in range(N):
            if abs(sr-i) + abs(sc-j) <= center:
                total += price[i][j]
    print(f"#{tc} {total}")