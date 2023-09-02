T = int(input())
for tc in range(1, T + 1):
    bina = input()
    tri = list(input())
    x = int(bina, 2)
    b_l = len(bina)
    check_money = []
    result = 0
    # 2진수 정확한 송금액 일 수 있는 수들 모음
    for i in range(b_l):
        change_b = list(bina[:])
        if x & (1 << i):
            change_b[b_l - i - 1] = "0"
            check_money.append(int("".join(change_b), 2))
        else:
            change_b[b_l - i - 1] = "1"
            check_money.append(int("".join(change_b), 2))
    for i in range(len(tri)):
        for j in range(1, 3):
            change_t = tri[:]
            change_t[i] = str((int(tri[i]) + j) % 3)
            if int("".join(change_t), 3) in check_money:
                result = int("".join(change_t), 3)
                break
        if result:
            break
    print(f"#{tc} {result}")

