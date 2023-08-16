T = int(input())


def turn(num_arr, m):
    # 전치 행렬을 취한 후 각 행들을 뒤집어 준다.
    for i in range(m):
        for j in range(m):
            if i < j:
                num_arr[i][j], num_arr[j][i] = num_arr[j][i], num_arr[i][j]
        num_arr[i].reverse()
    return num_arr


for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    result = [[0] * 3 for _ in range(N)]
    print(f"#{tc}")
    for i in range(3):
        degree = turn(arr, N)
        for j in range(N):
            result[j][i] = ''.join(degree[j])
    for k in range(N):
        print(*result[k])
