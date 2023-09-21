from heapq import heappush, heappop

# MST 문제 최소신장 트리 => prim 알고리즘 활용해서
def prim(start):
    heap = []
    # MST : 방문 노드 체크를 위한
    MST = [0] * (V+1)
    heappush(heap, (0, start))
    sum_weight = 0
    # heap이 비어 있을 때 까지 진행
    while heap:
        weight, v = heappop(heap)
        # 이미 방문한 노드라면 방문 X
        if MST[v]:
            continue
        MST[v] = 1
        sum_weight += weight
        for next in range(V+1):
            if graph[v][next] == 0:
                continue
            if MST[next] == 1:
                continue
            heappush(heap, (graph[v][next], next))
    return sum_weight

T = int(input())
for tc in range(1, T + 1):
    # V : 노드 마지막 번호 E : 간선 개수
    V, E = map(int, input().split())
    # 인접 행열을 사용 해서 간선 정보 저장
    graph = [[0] * (V + 1) for _ in range(V+1)]
    for i in range(E):
        # f : 시작 정점 t : 도착 정점 w : 간선 가중치
        # 방향이 존재하지 않는 그래프 => 양방향이라는 소리
        f, t, w = map(int, input().split())
        graph[f][t] = w
        graph[t][f] = w
    # 그래프는 다 저장 했고 prim 알고리즘 구현 후 실행
    print(f"#{tc} {prim(0)}")
