def conect(s, e):
    visited = [0] * (v + 1)
    q = []
    # 일단 시작 노드를 큐에 넣어준다
    q.append(s)
    # queue가 비어있지 않다면 계속 진행
    while q:
        st = q.pop(0)
        for i in info[st]:
            # 현재 노드에서 갈 수 있는 노드 중에 도착노드가 종료 된다면
            # 해당 노드의 값에서 +1 값을 리턴
            if i == e:
                return visited[st] + 1
            # i가 도착 노드가 아니라면
            else:
                # 방문하지 않았다면 방문해주고 q에 넣기
                if visited[i] == 0:
                    visited[i] = visited[st] + 1
                    q.append(i)
    return 0


T = int(input())
for tc in range(1, T + 1):
    # v : 노드 개수 e : 간선 정보 갯수
    v, e = map(int, input().split())
    # 인접 리스트에 간선 정보를 저장
    info = [[] for _ in range(v + 1)]
    for i in range(e):
        s, c = map(int, input().split())
        # 방향이 없는 간선 정보이므로 양쪽으로 모두 저장해 주어야 한다.
        info[s].append(c)
        info[c].append(s)
    # 노드의 번호가 1 부터 있으므로 v+1개의 방문 배열을 만들어 준다.
    start, end = map(int, input().split())
    answer = conect(start, end)
    print(f"#{tc} {answer}")