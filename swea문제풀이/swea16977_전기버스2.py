def min_charge(batt, change, st, end):
    global min_change
    if min_change <= change:
        return
    # 종료 조건
    if end >= N-1:
        if min_change > change:
            min_change = change
        return
    # 현 위치에서 갈 수 있는 모든 경우에 대해서 재귀 호출
    for i in range(1, batt + 1):
        if i < N:
            min_charge(charge[st + i], change + 1, st + i, charge[st+i] + st + i)


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]
    charge = arr[1:]
    min_change = 99999999
    start_charge = charge[0]
    min_charge(start_charge, 0, 0, start_charge)
    print(f"#{tc} {min_change}")
