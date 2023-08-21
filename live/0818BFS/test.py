def is_369(s):
    if s // 10 == 3 or s // 10 == 6 or s // 10 == 9:
        return s
    elif s % 10 == 3 or s % 10 == 6 or s % 10 == 9:
        return s
    else:
        return 0


N = int(input())
for i in range(1, N + 1):
    # 순서대로 차례대로 숫자가 들어간다.
    # 각 자릿수에 3,6,9가 포함되어 있다면 그 숫자만큼 _출력
    if is_369(i):
        string = str(i)
        clap = 0
        for j in string:
            if j == "3" or j == "6" or j == "9":
                clap += 1
        print("-" * clap, end=" ")
    else:
        print(i, end=" ")
