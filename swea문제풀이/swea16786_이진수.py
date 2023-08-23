T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    N = int(N)
    bina = ""
    for i in range(N):
        num = int(M[i], 16)
        for j in range(3, -1, -1):
            if num & (1 << j):
                bina += "1"
            else:
                bina += "0"
    print(f"#{tc} {bina}")

'''
T = int(input())
dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
for tc in range(1, T + 1):
    N, M = input().split()
    N = int(N)
    bina = ""
    for i in range(N):
        num = int(M[i], 16)
        ex = 3
        for j in range(4):
            if num - 2 ** ex >= 0:
                num = num - 2 ** ex
                bina += "1"
                ex -= 1
            else:
                bina += "0"
                ex -= 1

    print(f"#{tc} {bina}")


'''