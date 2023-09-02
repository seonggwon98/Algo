T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dock_time = []
    for i in range(N):
        dock_time.append(list(map(int, input().split())))
    dock_time.sort(key=lambda x: x[1])
    dock_time = [[0, 0]] + dock_time
    S = []
    j = 0
    for i in range(1, N+1):
        if dock_time[i][0] >= dock_time[j][1]:
            S.append(i)
            j = i
    print(f"#{tc} {len(S)}")
