def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N and arr[r][c] != "1"


def is_valid2(r, c, state):
    if state == "가로":
        return 0 <= r < N - 1 and 0 <= c < N - 1 and arr[r][c + 1] == "1"
    elif state == "대각":
        return 0 <= r < N - 1 and 0 <= c < N - 1 and arr[r - 1][c - 1] == "1"
    elif state == "세로":
        return 0 <= r < N - 1 and 0 <= c < N - 1 and arr[r + 1][c] == "1"


def move(r, c, state):
    global count
    if (r, c) == (N - 1, N - 1):
        count += 1
        return
    elif is_valid2(r, c, state):
        return

    # 상태 따라 갈 수 있는 방향이 있음
    for d in range(3):
        if state == "가로" and d != 1:
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and d == 0:
                move(nr, nc, "가로")
            if is_valid(nr, nc) and d == 2:
                move(nr, nc, "대각")
        if state == "세로" and d != 0:
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and d == 1:
                move(nr, nc, "세로")
            if is_valid(nr, nc) and d == 2:
                move(nr, nc, "대각")
        if state == "대각":
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and d == 0:
                move(nr, nc, "가로")
            if is_valid(nr, nc) and d == 1:
                move(nr, nc, "세로")
            if is_valid(nr, nc) and d == 2:
                move(nr, nc, "대각")


# 0 : 가로 1 : 세로 2 : 대각
dr = [0, 1, 1]
dc = [1, 0, 1]
N = int(input())
arr = [list(input().split()) for _ in range(N)]
# 파이프가 세로로 놓여 있었는지 가로로 놓여있었는지 확인법은
# 파이프의 위치 변화를 살펴 보면 가능 할 거 같음
# 하지만 벽이 있다면 갈수 없음 미끌 ? 가로나 세로는 해당 방향으로 벽이 없으면 가능하지만 대각선은 놓을 위치의
# 자기 자신, 좌, 상이 모두 빈 칸이어야 한다.
r = nr = c = 0
nc = 1
state = "가로"
count = 0
move(nr, nc, state)
print(count)
