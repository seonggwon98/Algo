T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리를 가장 많이 잡았을 경우 변수 지정
    max_catch = 0
    # 주어진 행열에서 파리채의 사이즈를 뺀 인덱스까지 진행해야 하므로 범위를 (N - M +1)으로설정
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리채에 잡힌 파리의 합 변수 초기화해주고
            # 위의 반복문에서 행열을 순서대로 진행하면서 주어진 파리채의 사이즈를 한칸씩 옮겨가며 해당 값들을 더해준다
            # arr[i][j] 시작하여 주어진 M*M 사이즈로 순회 하면서 해당 값들을 더해주어 최댓값을 찾아준다.
            sum_catch = 0
            for k in range(i, i + M):
                for p in range(j, j + M):
                    sum_catch += arr[k][p]
            if max_catch < sum_catch:
                max_catch = sum_catch
    print(f"#{tc} {max_catch}")
