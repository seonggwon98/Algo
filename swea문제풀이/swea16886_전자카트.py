def area_circuit(i, n):
    global min_battery
    if i == n:
        p[n] = 1
        now_sum = 0
        for i in range(n):
            now_sum += arr[p[i]-1][p[i + 1]-1]
        if min_battery > now_sum:
            min_battery = now_sum
        return
    # 1을 제외한 모든 원소에 대한 순열을 만든다.
    for j in range(2, n + 1):
        if not used[j]:
            p[i] = j
            used[j] = 1
            area_circuit(i + 1, n)
            used[j] = 0


# 사무실 출발 관리구역 돌고 다시 사무실로
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # N 구역까지 있기 때문에 N+1개 만듬
    used = [0] * (N + 1)
    p = [0] * (N + 1)
    p[0] = 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_battery = N * N * 100 + 1
    # 순열의 1번 인덱스 부터 저장
    area_circuit(1, N)
    print(f"#{tc} {min_battery}")
