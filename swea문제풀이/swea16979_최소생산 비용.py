def min_cost(arr, row, now):
    global min_ct
    # 종료 조건
    # 기본적으로 마지막 행 까지 제품을 한개씩 다 골랐다면 종료
    # 제품을 다 고르지 않았지만 최소 생산 비용보다 
    # 비용이 크다면 종료 시켜 주어야 한다
    if row == N or min_ct <= now:
        if min_ct > now:
            min_ct = now
        return
    # 재귀 호출
    # 공장 한 곳당 제품 한개
    for i in range(N):
        # 해당 공장에서 다른 제품을 생산했는지 열을 i번째 열을 확인
        possible = True
        for j in range(N):
            if production[j][i] == 1:
                possible = False
                break
        # 제품을 생산 할 수 있다면 해당 제품 생산하고 다음 위치로 이동
        if possible:
            production[row][i] = 1
            min_cost(arr, row + 1, now + costs[row][i])
            production[row][i] = 0


T = int(input())
for tc in range(1, T + 1):
    # N 은 제품의 개수
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    production = [[0]*N for _ in range(N)]
    min_ct = 1600
    min_cost(costs, 0, 0)
    print(f"#{tc} {min_ct}")