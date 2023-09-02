T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(1, 1 << N):
        # i번째 부분 집합에 j번째 비트가 존재하는지 확인
        subset = []
        for j in range(N - 1, -1, -1):
            if i & (1 << j):
                if A[j] > K:
                    subset.append(A[j])
                    break
                subset.append(A[j])
        if sum(subset) == K:
            count += 1
    print(f"#{tc} {count}")
