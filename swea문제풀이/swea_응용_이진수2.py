T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    bin_string = ""
    while True:
        if N <= 0:
            break
        if len(bin_string) > 12:
            bin_string = "overflow"
            break
        if N * 2 >= 1:
            N = N * 2 - 1
            bin_string += "1"
        else:
            N = N * 2
            bin_string += "0"
    print(f"#{tc} {bin_string}")



