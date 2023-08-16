T = int(input())
for tc in range(1, T + 1):
    # 당근의 개수
    N = int(input())
    # arr : 당근의 크기가 적힌 리스트
    arr = list(map(int, input().split()))
    # 연속으로 커지지 않는 경우 최소 길이는 1 이므로 count는 1 부터 시작
    max_count = 1
    count = 1
    # arr을 순회하면서 그 전 당근과 비교했을 때 크다면 카운트 증가
    for i in range(1, N):
        if arr[i] > arr[i-1]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 1
    print(f"#{tc} {max_count}")