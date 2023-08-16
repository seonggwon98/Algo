T = 10
for t in range(1, T + 1):
    # tc : 테스트 케이스의 번호 N : 길의 총 개수
    tc, N = map(int, input().split())
    # 한 줄로 나열된 순서쌍이 주어지므로 해당 줄에서 순서에 맞추어
    # 순서쌍을 뽑아내어 간선의 정보를 저장 해야 한다.
    # 인접 리스트로 받아볼 생각 X 이번 건 인접 배열로 접근하는 편이 좋다
    # pair_arr : 나열된 순서쌍 모음
    pair_arr = list(map(int, input().split()))
    abj_m = [[0] * 100 for _ in range(100)]
    for i in range(N):
        abj_m[pair_arr[2 * i]][pair_arr[2 * i + 1]] = 1
    stack = []
    visited = [0] * 100
    # 길을 찾을 경우 1로 바꾸어줄 변수
    # 시작 위치는 항상 0
    nn = 0
    visited[nn] = 1
    stack.append(nn)
    answer = 0
    # 일단 길을 찾을 때까지 반복 하지만 길을 전부 탐색 했는데도 A=>B 경로가 존재하지 않을 경우
    # break로 종료
    while not (answer):
        # 해당 번호의 노드가 갈 수 있는 길이 정리된 인접 리스트로 접근 하여 방문 여부 파악 후
        # 해당 노드를 방문한 적이 없을 경우 해당 노드로 현재 위치를 옮기면서 스택에 추가
        for i in range(100):
            if abj_m[nn][99] == 1:
                answer = 1
                break
            if abj_m[nn][i] == 1 and visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                nn = i
                break
        # 탐색 종료 후 갈 길이 없을 경우
        else:
            # 스택이 존재한다면 뒤로 갈수 있으므로 현재 위치를 뒤의 위치로 되돌아감
            if stack:
                nn = stack.pop()
            else:
                break
    print(f"#{tc} {answer}")
