def swap(cnt):
    # 종료 조건 : 교환 횟수를 다 소모 했다면
    # 바꾼 결과물을 숫자로 바꿔서 최대 상금 계산
    global result
    if cnt == change:
        reward = int("".join(info))
        if result < reward:
            result = reward
    # 최댓값으로의 정렬은 l번 진행되면 완료가 된다 그 이후로 진행될 경우
    elif cnt > l-1:
        # 요소 중에 중복된 것이 없으므로 끝에 가장 작은 수와 그다음 작은수 자리 변경
        if len(set(info)) == l:
            info[-1], info[-2] = info[-2], info[-1]
            swap(cnt + 1)
        # 중복 된거 존재시 중복 된거 끼리 변경가능하므로 그대로 값 저장
        else:
            swap(cnt + 1)
    else:
        for i in range(len(info) - 1):
            for j in range(i + 1, len(info)):
                info[i], info[j] = info[j], info[i]
                swap(cnt + 1)
                info[i], info[j] = info[j], info[i]


T = int(input())
for tc in range(1, T + 1):
    info, change = input().split()
    info = list(info)
    change = int(change)
    l = len(info)
    result = 0
    swap(0)
    print(f"#{tc} {result}")
