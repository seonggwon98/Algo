def get_code(r, m):
    for i in range(r):
        even = 0
        odd = 0
        for j in range(m - 1, 6, -1):
            # 뒤에서부터 1을 찾아 해당 자리가 암호코드의 끝 인 걸 활용하여 그 숫자 부터 해서 56개의 비트를 7개씩 끊어가면서 암호를 확인
            if code[i][j] == "1":
                # 뒤에서부터 읽어올 것이기 때문에 몇 번째 숫자인지 알려주기 위해서 count 생성
                count = 8
                for k in range(j, j - 56, -7):
                    code_num = code[i][k - 6: k + 1]
                    # 해당 암호와 변환표를 비교하여 변환표의 인덱스가 변환한 번호
                    # count   홀수 일 때 odd 짝수 라면  even에 변환된 번호 더해준다.
                    for n in range(10):
                        if code_num == code_table[n]:
                            if count % 2:
                                odd += n
                                count -= 1
                                break
                            else:
                                even += n
                                count -= 1
                                break
                # 모든 암호를 다 확인했다면 정상적인 암호인지 확인
                if (odd * 3 + even) % 10 == 0:
                    return odd + even
                else:
                    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    code_table = ["0001101", "0011001", "0010011", "0111101", "0100011",
                  "0110001", "0101111", "0111011", "0110111", "0001011"]
    result = get_code(N, M)
    print(f"#{tc} {result}")
