def max_(max_num, number):
    if max_num < number:
        return number
    else:
        return max_num

for t in range(10):
    tc = int(input())
    num_arr = [list(map(int, input().split())) for _ in range(100)]
    # 최종합 변수와 대각선의 합 변수는 반복이 다 끝난후 필요하기 때문에 반복문 시작전 초기화
    max_num = 0
    sum_dig = 0
    sum_reversed_dig = 0
    for i in range(100):
        # 각 행과 열의 합은 i의 값이 증가할 때 새로 갱신 되어야 하므로 2번째 for문 전에 초기화
        sum_row = 0
        sum_col = 0
        for j in range(100):
            # 각 행과 열의 합 행은 그대로 i j , 열은 j i   => i 값이 고정일때 j값이 증가되므로
            sum_row += num_arr[i][j]
            sum_col += num_arr[j][i]
            # 대각선의 합은 i == j 가 같을 경우
            if i == j:
                sum_dig += num_arr[i][j]
            # 반대 대각선의 겨우 i  가 증가할수록 열의 위치는 감소하므로 
            if i == (99 - j):
                sum_reversed_dig += num_arr[i][j]
        # 각 행과 열의 합과 최댓값 비교
        max_num = max_(max_num, sum_row)
        max_num = max_(max_num, sum_col)
    # 대각선의 합은 행열을 다 순회 후 알 수 있으므로 다 끝난 후 최댓값과 비교
    max_num = max_(max_num, sum_dig)
    max_num = max_(max_num, sum_reversed_dig)

    print(f"#{tc} {max_num}")