def contact(s):
    visited = [0] * 101
    q = []
    q.append(s)
    visited[s] = 0
    while q:
        nn = q.pop(0)
        # 해당 노드에서 갈 수 있는 다음 노드 방문
        for i in node[nn]:
            # 방문하지 않았다면
            if visited[i] == 0:
                # 방문 처리를 하고
                visited[i] = visited[nn] + 1
                # 해당 노드를 queue에 더해준다
                q.append(i)
    last = visited[nn]
    # q가 비었다는 말은 갈 수 있는 노드를 다 돌았다는 뜻이고 마지막 노드의
    # visited 값을 가장 나중에 연락 받는 사람들이 몇번째 인지 구하고
    # 큰 번호의 노드부터 보면서 마지막 연락 받은 사람인지 확인
    for j in range(100, -1, -1):
        if visited[j] == last:
            return j


T = 10
for tc in range(1, T + 1):
    # N : 입력 받는 데이터의 길이 S : 시작점
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    # 노드 최대 갯수 100 하지만 최대 번호가 100 그러므로 101 범위 지정
    node = [[] for _ in range(101)]
    for i in range(N // 2):
        f, t = arr[2 * i], arr[2 * i + 1]
        node[f].append(t)
    print(f"#{tc} {contact(S)}")


