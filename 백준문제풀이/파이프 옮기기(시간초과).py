def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N and arr[r][c] != "1"


def right(r, c):
    nr = r + dr[0]
    nc = c + dc[0]
    if is_valid(nr, nc):
        move(nr, nc, 0)


def down(r, c):
    nr = r + dr[1]
    nc = c + dc[1]
    if is_valid(nr, nc):
        move(nr, nc, 1)


def dig(r, c):
    nr = r + dr[2]
    nc = c + dc[2]
    if is_valid(nr, nc) and arr[nr - 1][nc] != "1" and arr[nr][nc - 1] != "1":
        move(nr, nc, 2)


def move(r, c, state):
    global count
    # 도착 지점에 왔다면 함수를 종료 해주고 count를 증가 시켜 준다
    if (r, c) == (N - 1, N - 1):
        count += 1
        return
    if state == 0:

        right(r, c)
        dig(r, c)
    elif state == 1:
        down(r, c)
        dig(r, c)
    else:
        right(r, c)
        down(r, c)
        dig(r, c)


# 0 : 가로 1 : 세로 2 : 대각
dr = [0, 1, 1]
dc = [1, 0, 1]
N = int(input())
arr = [list(input().split()) for _ in range(N)]
# 파이프가 세로로 놓여 있었는지 가로로 놓여있었는지 확인법은
# 파이프의 위치 변화를 살펴 보면 가능 할 거 같음
# 하지만 벽이 있다면 갈수 없음 미끌 ? 가로나 세로는 해당 방향으로 벽이 없으면 가능하지만 대각선은 놓을 위치의
# 자기 자신, 좌, 상이 모두 빈 칸이어야 한다.
sr, sc = 0, 1
state = 0
count = 0
move(sr, sc, state)
print(count)
