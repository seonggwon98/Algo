hex1 = "0DEC"


def solution(hex_string):
    # 16 진수를 2진수로 변환시 문자 하나당 4비트씩 필요하므로
    l = len(hex_string) * 4
    # 해당 16 진수를 10진수로 변환
    x = int(hex_string, 16)
    print(x)
    print(bin(x))
    bin_string = ""
    for i in range(l - 1, -1, -1):
        bin_string += "1" if x & (1 << i) else "0"
    print(bin_string)

solution(hex1)