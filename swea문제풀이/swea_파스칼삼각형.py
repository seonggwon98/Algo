T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 삼각형 모양의 1로 이루어진 배열 만들기
    tri = [[1]*i for i in range(1, N + 1)]
    # 0행과 1행은 조건을 만족 했으므로 2행부터 시작
    for i in range(2, N):
        # 2행 부터는 처음 열과 마지막 열을 제외한 위치의 값들만 바꾸어 주면 된다. 
        for j in range(1, i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
    print(f"#{tc}")
    for k in range(N):
        print(*tri[k])