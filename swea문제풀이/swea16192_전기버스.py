T = int(input())
for tc in range(1, T + 1):
    # K -> 한번 충전 으로 갈 수 있는 정류장 수
    # N -> 종점 정류장 번호
    # M -> 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())
    # 충전소가 설치된 정류장 번호
    station_with_charge = list(map(int, input().split()))
    now_bus = 0  # 현재 버스위치
    charge = K  # 충전량
    count_charge = 0  # 충전 횟수
    # 충전기 설치가 잘못 되었다는 말은 곧 충전소 사이의 거리가 
    # 한번으로 충전으로 갈 수있는 값 K 보다 크다는 말이므로 밑에 while문은 실행되지 않고 넘어간다.
    for i in range(M-1):
        if station_with_charge[i + 1] - station_with_charge[i] > K:
            now_bus = N+1
            break
            
    while now_bus <= N:
        # 
        find_charge = False
        now_bus += 1
        charge -= 1
        max_step = now_bus + charge
        if max_step >= N:
            break
        # 정류장 번호는 최대 멀리 갈 수 있는 거리에
        # 충전소가 있는 정류장이 있다면 해당 위치로 이동하고
        # 충전량은 리셋 충전 횟수는 1증가

        for j in range(max_step, max_step - charge -1, -1):
            for station in station_with_charge:
                if j < station:
                    continue
                if j == station:
                    now_bus = station
                    charge = K
                    count_charge += 1
                    find_charge = True
                    break
            if find_charge:
                break
    print(f"#{tc} {count_charge}")






