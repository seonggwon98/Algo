def find_code(bin_st, n):
    # e가 0보다 클 때만 반복
    e = n
    # 배열에서 만들어진 code를 담을 리스트
    code = []
    while e > 0:
        # 암호코드의 배율? 가로길이를 찾기 위한 리스트
        # 뒤에서 부터 읽고 와서 1과 0이 바뀐다면 count 저장 후 초기화
        # ratio 길이가 4가 된다면 종료 하여 해당 값 중 가장 작은 값이 선의 굵기가 된다.
        ratio = []
        count = 0
        for i in range(e, 0, -1):
            count += 1
            if bin_st[i] != bin_st[i - 1]:
                ratio.append(count)
                count = 0
            # ratio가 4개 일 때 리스트의 최솟값으로 해당 코드의 암호의 굵기 알 수 있음
            if len(ratio) == 4:
                thick = min(ratio)
                break
        # 해당 선의 굵기에 맞추어 가로길이를 조정하면서 반복을 돌며 암호코드 저장
        bin_str = ""
        for st in range(e, e - 56 * thick + 1, -7 * thick):
            # 암호코드를 선의 굵기 만큼 건너 뛰면서 암호 변환표의 암호들과 비교
            code_string = bin_st[st - 7 * thick + 1: st + 1: thick]
            bin_str = code_table[code_string] + bin_str
        code.append(list(map(int, bin_str)))
        # 첫번째 암호표를 찾고 나서 그 후로도 더 암호 코드가 있는지 확인 하기 위한 반복 구문
        # 찾는다면 끝 점을 다시 조정 해서 위의 while 반복
        for k in range(e - 56 * thick -2, -1, -1):
            if bin_st[k] == "1":
                e = k
                break
        else:
            e = -1
    return code


def get_result(code):
    even = 0
    odd = 0
    for j in range(7):
        if j % 2 == 0:
            even += code[j]
        else:
            odd += code[j]
    if (even * 3 + odd + code[7]) % 10 == 0:
        return sum(code)
    else:
        return 0


# 암호변환표
code_table = {"0001101": "0",
              "0011001": "1",
              "0010011": "2",
              "0111101": "3",
              "0100011": "4",
              "0110001": "5",
              "0101111": "6",
              "0111011": "7",
              "0110111": "8",
              "0001011": "9"
              }
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(set([input() for _ in range(N)]))
    arr_l = len(arr)
    code_list = []
    result = 0
    for i in range(arr_l):
        # 암호코드는 16진수로 이루어져 있으며 배열의 뒤에서 부터 봐 가면서
        # 0이 아닌 값이 들어 있다면 거기서 부터 문자열에 더해가며 계산
        l = len(arr[i]) * 4
        x = int(arr[i], 16)
        bin_string = ""
        # 먼저 10진수로 변환된 x를 이진수로 변환 후 뒤에서 1이 있는 자리가 암호 코드의 끝 자리
        # 제일 먼저 완성 되는 코드의 숫자 비율을 먼저 파악한 후 해당 암호 코드의 배율을 찾아 나간다.
        # 같은 행에 암호코드가 여러개 존재 할 수 있기 때문에 또다시 1을 찾는다.
        for j in range(l - 1, -1, -1):
            bin_string += "1" if x & (1 << j) else "0"
        if "1" in bin_string:
            for n in range(l - 1, -1, -1):
                if bin_string[n] == "1":
                    code = find_code(bin_string, n)
                    for k in range(len(code)):
                        if code[k] not in code_list:
                            code_list.append(code[k])
                    break

    for co in code_list:
        result += get_result(co)
    print(f"#{tc} {result}")