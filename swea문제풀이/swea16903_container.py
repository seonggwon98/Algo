T = int(input())
for tc in range(1, T + 1):
    # N : 컨테이너 수 M : 트럭 수
    N, M = map(int, input().split())
    # 컨테이너 무게
    w = list(map(int, input().split()))
    # 트럭 적대용량
    t = list(map(int, input().split()))
    w.sort()
    t.sort()
    # 정렬 후 큰 차 부터 가장 무거운 무게와 비교해 가며 큰 차가 가져갈 수 있으면 가져 가고 pop
    weight = 0
    for i in range(N - 1, -1, -1):
        for j in range(len(t)-1, -1, -1):
            if w[i] <= t[j]:
                weight += w[i]
                t.pop()
                break
        if not t:
            break
    print(f"#{tc} {weight}")
