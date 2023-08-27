switch_num = int(input())
# 스위치 번호는 index + 1
sw_state = list(input().split())
st_num = int(input())
# st_info : 성별과 받은 숫자가 주어짐
st_info = [list(input().split()) for _ in range(st_num)]
boy, girl = "1", "2"
l = len(sw_state)
for i in range(st_num):
    gender = st_info[i][0]
    num = int(st_info[i][1])
    if gender == boy:
        for j in range(num - 1, l, num):
            if sw_state[j] == "1":
                sw_state[j] = "0"
            else:
                sw_state[j] = "1"
    # 여자라면 # 해당 숫자를 기준으로 양 옆을 살펴 가며 대칭일 경우 자기 자신을 포함한 해당 구간의 상태를 전부 바꾸어 준다.
    else:
        k = 1
        real_num = num - 1
        while real_num - k >= 0 and real_num + k < l:
            if sw_state[real_num - k] == sw_state[real_num + k]:
                if sw_state[real_num - k] == "1":
                    sw_state[real_num- k] = "0"
                    sw_state[real_num  + k] = "0"
                    k += 1
                else:
                    sw_state[real_num - k] = "1"
                    sw_state[real_num + k] = "1"
                    k += 1
            else:
                break
        if sw_state[real_num] == "1":
            sw_state[real_num] = "0"
        else:
            sw_state[real_num] = "1"

for j in range(0, l, 20):
    for n in range(j, j + 20):
        if n > l - 1:
            break
        print(sw_state[n], end=" ")
    print()

