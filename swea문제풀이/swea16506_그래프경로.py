T = int(input())
for tc in range(1, T + 1):
    # V는 총 노드의 개수 E는 연결한 간선의 개수
    V, E = map(int, input().split())
    # 일단 총 노드의 개수에 맞추어 배열 생성
    adj_l = [[] for _ in range(V+1)]
    # E개의 간선에 대한 정보를 adj_l에 저장
    for i in range(E):
        s, e = map(int, input().split())
        # 방향성이 있는 그래프이므로 해당 방향만 간선 정보에 저장
        adj_l[s].append(e)
    # 경로의 존재를 확인할 출발 노드와 도착 노드가 주어진다.
    start_node, end_node = map(int, input().split())
    # 빈 스택과 방문여부 배열을 만들어 준 후 탐색을 진행해줄 시작 변수를 지정 하고 방문 처리
    stack = []
    visited = [0] * (V + 1)
    nn = start_node
    visited[nn] = 1
    # 주어진 출발 노드에서 도착 노드까지의 경로가 존재하면 1로 바뀜
    answer = 0
    # 탐색을 시작한다.
    while not(answer):
        # 해당 노드의 간선 정보는 리스트로 저장 되어 있으므로 방문처리 여부 확인 후 해당 노드로 이동
        for j in adj_l[nn]:
            # 해당 간선의 노드가 방문 처리 되지 않았다면
            # 현재 노드가 해당 노드가 되고 해당 노드를 방문 처리 해준 후 스택에 삽입하고 해당 반복을 종료해준다.
            if visited[j] == 0:
                stack.append(j)
                visited[j] = 1
                nn = j
                if j == end_node:
                    answer = 1
                break
        else:
            # 탐색을 전부 했는데도 다음 노드가 없다면 전 노드의 갈림길을 확인해 보아야 한다.
            if stack:
                nn = stack.pop()
            else:
                break
    print(f"#{tc} {answer}")
