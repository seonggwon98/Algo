# 각 변에 16 진수 보물상자, 뚜껑 시계방향으로 한번 돌리면 한칸 이동
# 변이 4개이므로 회전 횟수는 전체 숫자 // 4 회전 하면서 제일 처음 수 제일 뒤쪽에 붙이는 반 시계 방향으로 진행해도
# 숫자는 똑같이 생성 된다 그 중에 K번째 큰 수 찾으면 된다.
def make_num(li):
    # N//4개씩 끊어서 숫자 생성
    i = 0
    num = ""
    while i < N + 1:
        if i != 0 and i % (N // 4) == 0:
            num_box.add(int(num, 16))
            num = ""
        if i == N:
            return
        num += li[i]
        i += 1


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())
    spin_arr = arr[:]
    num_box = set()
    result = []
    make_num(arr)
    for i in range(1, N // 4 + 1):
        tmp = spin_arr.pop(0)
        spin_arr.append(tmp)
        make_num(spin_arr)
    num_box = list(num_box)
    num_box.sort(reverse=True)
    print(f"#{tc} {num_box[K - 1]}")
