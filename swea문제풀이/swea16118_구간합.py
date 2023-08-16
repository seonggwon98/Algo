T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    max_sum = 1
    min_sum = 90000000
    for i in range(N-M+1):
        sum_arr = 0
        for j in range(i, i+ M):
            sum_arr += arr[j]
        if sum_arr > max_sum:
            max_sum = sum_arr
        if sum_arr < min_sum:
            min_sum = sum_arr
    print(f"#{tc} {max_sum -min_sum}") 
            