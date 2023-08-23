def get_code(r, m):
    for i in range(r):
        even = 0
        odd = 0
        for j in range(m - 1, 6, -1):
            if code[i][j] == "1":
                count = 8
                for k in range(j, j - 57, -7):
                    code_num = code[i][k - 6: k + 1]
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
