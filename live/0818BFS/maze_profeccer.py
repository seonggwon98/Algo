#        0    1    2    3    4    5    6    7    8    9
node = ["x", "A", "B", "C", "D", "E", "F", "G", "H", "I"]

"""
그래프의 정보
정점의 개수 V, 간선의 개수 E
V = 9 , E = 8
9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9
"""
"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
"""

# G : 그래프 정보(인접 행렬, 인접리스트)
# v : 시작 정점 번호
# N : 정점의 개수
def bfs(G, v, N):
    # 중복 방문 방지를 위한 방문 체크 배열
    visited = [0] * (N + 1)
    # 큐 생성
    q = []
    # 시작점을 큐에 넣은 상태로 방문 시작
    q.append(v)
    visited[v] = 1

    # 큐가 빌때까지 계속 방문
    while q:
        # 큐에서 방문할곳 하나 꺼내옴
        t = q.pop(0)
        print(t, end=" ")
        # 현재 정점 t에서 연결된 모든 정점 i를 탐색
        for i in G[t]:
            # i번 정점을 방문한적이 없다면
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 넣고
                q.append(i)
                # 방문처리 동시에 지나온 간선 개수
                visited[i] = visited[t] + 1

    print(visited)


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]  # 인접 리스트

for i in range(E):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

bfs(G, 1, V)
