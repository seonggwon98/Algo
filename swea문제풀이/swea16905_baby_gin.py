def is_run(li):
    count = 1
    for i in range(1, len(li)):
        if li[i - 1] + 1 == li[i]:
            count += 1
            if count == 3:
                return 1
        else:
            count = 0
    if count < 3:
        return 0


def is_triplet(li):
    count = 1
    for i in range(1, len(li)):
        if li[i] != li[i - 1]:
            count = 0
        count += 1
        if count == 3:
            return 1
    if count < 3:
        return 0

# 입력으로 들어온 리스트에서 순열을 만들어 run, triplet 있다면 전역변수에 유무 저장
def baby_gin(a, n, li):
    global check
    if a == n:
        if is_run(perm) or is_triplet(perm):
            check = 1
        return
    for i in range(n):
        if not used[i]:
            perm[a] = li[i]
            used[i] = 1
            baby_gin(a + 1, n, li)
            used[i] = 0


T = int(input())
for tc in range(1, T + 1):
    li = list(map(int, input().split()))
    used = [0] * 6
    check = 0
    player1 = []
    player2 = []
    # 0과 짝수일때는 플레이어 1이 카드를 홀수일 경우 플레이어 2가 카드를 가져간다
    # 순열의 크기가 변하기 때문에 일단 [0] 배열 한개로 초기화
    for i in range(len(li)):
        perm = [0]
        if i % 2 == 0:
            player1.append(li[i])
            # 길이가 3 개 이상이라면
            if len(player1) > 2:
                # 순열을 담을 배열의 사이즈 조절
                perm = perm * len(player1)
                baby_gin(0, len(player1), player1)
                # 베이비진 유무 판단 있을 시 출력 후 반복 종료
                if check == 1:
                    print(f"#{tc} {1}")
                    break
        else:
            player2.append(li[i])
            if len(player2) > 2:
                perm = perm * len(player2)
                baby_gin(0, len(player2), player2)
                if check == 1:
                    print(f"#{tc} {2}")
                    break
    # 반복이 끝나고도 출력된 것이 없다면 무승부 출력
    else:
        if check == 0:
            print(f"#{tc} {0}")
