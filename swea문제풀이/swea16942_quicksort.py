def partition(A, l, r):
    # 피봇 정해주기
    p = A[l]
    # i와 j 위치 각각 잡아주기
    i, j = l, r
    # A 리스트에서 i를 증가 시키면서 해당 위치가 p보다 크면 멈춘다.
    # j 는 감소시키면서 p보다 작은 값이 있다면 멈춘다.
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        # 교차 하지 않고 i와 j의 위치를 찾았다면 두 위치를 바꾸어 준다
        if i < j:
            A[i], A[j] = A[j], A[i]
    # 반복이 끝나면 p과 j의 위치를 바꾸어 준다 p의 해당 위치는 앞으로 고정 이다.
    A[l], A[j] = A[j], A[l]
    # 해당 피봇의 위치 리턴
    return j


# A : 정렬할 대상 리스트
# l : 왼쪽 인덱스
# r : 오른쪽 인덱스
def quicksort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        # 고정된 위치를 찾은 곳을 제외한 나머지 왼쪽 오른쪽 부분에서 정렬을 진행한다.
        quicksort(A, l, s - 1)
        quicksort(A, s + 1, r)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    quicksort(A, 0, N - 1)
    print(f"#{tc} {A[N//2]}")
