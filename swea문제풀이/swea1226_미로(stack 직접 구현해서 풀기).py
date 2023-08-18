def start_point(n):  # 배열의 크기 n이 주어짐
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return i, j


def my_push(item):
    global top  # top 변수는 전역변수로 지정해야 모든 곳에서 동일하게 적용된다.
    # push는 stack에 넣어주는 작업만 하기 때문에 별도로 return은 없어도 됨
    top += 1
    stack[top] = item


def my_pop():
    global top
    # 스택이 비어있다면 뺄수 없음 오류 출력 디버깅용이라고 생각해도 됨
    # 기존의 스택의 탑 값을 반환하고 탑의 인덱스 1 감소
    if top == -1:
        print("underflow")
        return
    else:
        top -= 1
    # 기존 스택 top값을 반환 해줘야 하기 때문에 배열로 만든 스택이기에 값이 사라지는 것이 아님
    # 고로 top + 1의 값을 반환해주면 됨
    return stack[top + 1]


def is_value(nr, nc):
    return 0 <= nr < N and 0 <= nc < N


# 상 하 좌 우 순서 델타 배열 생성
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = 10
for t in range(T):
    tc = int(input())
    # 16 * 16의 2차원 배열이 주어짐
    maze = [list(map(int, input())) for _ in range(16)]
    # 100 배열은 큐로 풀어서 스택으로 접근해볼 생각
    # python의 append()와 pop()을 사용하지 않고 top을 통해 구현 예정이므로 스택의 크기가 어느정도 될지 고려
    # 아니면 my_push 함수에서 추가 할때마다 1개의 0배열을 계속해서 더해주어도 됨
    # 커 봤다 16 * 16
    N = 16
    # 스택을 만들어 주고 top의 위치 -1로 초기화 아직 스택은 비어 있기 때문에
    stack = [0] * N * N
    visited = [[0] * N for _ in range(N)]
    top = -1
    # 시작점 저장해 주고 스택에 저장 방문 처리도
    r, c = start_point(16)
    my_push((r, c))
    visited[r][c] = 1
    # 얼마나 반복해야하는지 알 수 없기 때문에 while 스택이 비어 있다면 더 이상 갈 곳이 없다는 말
    answer = 0
    while not answer:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if maze[nr][nc] == 3:
                answer = 1
                break
            if is_value(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                my_push((nr, nc))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            # for 문이 break 없이 종료 후 top의 위치가 -1이라면 스택이 비어 있다는 뜻 while 종료
            if top == -1:
                break
            # 스택이 차 있다면 계속 pop
            r, c = my_pop()

    print(f"#{tc} {answer}")
