T = int(input())
A = list(range(1,13))
for tc in range(1, T +1):
    N, K = map(int, input().split())
    set_len = len(A)
    count_sub = 0
    for i in range(1<<set_len):
        sum_set = 0 
        subset  = []
        for j in range(set_len):   # 원소의 개수 만큼 반복하며  i번째 부분 집합에 j번째 요소가 들어 있는지 확인
            if i & (1<<j):
                sum_set += A[j]
                subset.append(A[j])
        if len(subset) == N:
            if sum_set == K:
                count_sub += 1
    print(f"#{tc} {count_sub}")
    