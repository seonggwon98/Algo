T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 1
    for i in range(M, M - N,-1):
        result *= i
    x = 1

    for j in range(N, 0, -1):
        x *= j
    print(int(result/x))
