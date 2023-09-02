import copy


# N : 0 S : 1
# 붙어있는 옆날과 자성 다를 경우 반대 방향으로 회전
def r_spin(li):
    tmp = li.pop()
    li = [tmp] + li
    return li


def l_spin(li):
    tmp = li.pop(0)
    li.append(tmp)
    return li


def is_turn(li_1, li_2):
    return li_1[2] != li_2[6]


T = int(input())
for tc in range(1, T + 1):
    # K : 회전 횟수
    K = int(input())
    info = [list(map(int, input().split())) for _ in range(4)]
    change = [list(map(int, input().split())) for _ in range(K)]
    new_arr = info[:]

    for i in range(K):
        target, d = change[i]
        target = target - 1
        # 주어진 정보에 맞게 순서대로 자석들을 돌린다.
        if d == 1:
            arr = copy.deepcopy(info)
            new_arr[target] = r_spin(arr[target])
            nd = 1
            for j in range(target, 3):
                if is_turn(info[j], info[j + 1]):
                    if nd == 1:
                        new_arr[j + 1] = l_spin(arr[j + 1])
                        nd = -1
                    else:
                        new_arr[j + 1] = r_spin(arr[j + 1])
                        nd = 1
                else:
                    break
            nd = 1
            for k in range(target, 0, -1):
                if is_turn(info[k - 1], info[k]):
                    if nd == 1:
                        new_arr[k - 1] = l_spin(arr[k - 1])
                        nd = -1
                    else:
                        new_arr[k - 1] = r_spin(arr[k - 1])
                        nd = 1
                else:
                    break
        elif d == -1:
            arr = copy.deepcopy(info)
            new_arr[target] = l_spin(arr[target])
            nd = -1
            for j in range(target, 3):
                if is_turn(info[j], info[j + 1]):
                    if nd == 1:
                        new_arr[j + 1] = l_spin(arr[j + 1])
                        nd = -1
                    else:
                        new_arr[j + 1] = r_spin(arr[j + 1])
                        nd = 1
                else:
                    break
            nd = -1
            for k in range(target, 0, -1):
                if is_turn(info[k - 1], info[k]):
                    if nd == 1:
                        new_arr[k - 1] = l_spin(arr[k - 1])
                        nd = -1
                    else:
                        new_arr[k - 1] = r_spin(arr[k - 1])
                        nd = 1
                else:
                    break
        info = copy.deepcopy(new_arr)
    result = 0
    for i in range(4):
        if info[i][0] == 1:
            result += 2 ** i
    print(f"#{tc} {result}")
