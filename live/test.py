def find_code(pass_string):
    # 암호코드는 16진수로 이루어져 있으며 배열의 뒤에서 부터 봐 가면서
    # 0이 아닌 값이 들어 있다면 거기서 부터 문자열에 더해가며 계산
    l = len(pass_string) * 4
    x = int(pass_string, 16)
    bin_string = ""
    for i in range(l - 1, -1, -1):
        bin_string += "1" if x & (1 << i) else "0"
    if "1" in bin_string:
        for j in range(l - 1, -1, -1):
            if bin_string[j] == "1":
                pass


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    password = [input() for _ in range(N)]

    # 발견될 코드가 1개 이상이기 때문에 리스트에 담아준다.
    # 연달아서 있는 이진수의 코드를 4곳에 담아 가장 작은 값과 나머지의 비율을
    # 활용해서 코드의 가로길이를 구해야 한다.
    for i in range(N):
        pass
