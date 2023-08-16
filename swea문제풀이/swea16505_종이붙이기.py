def paper(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * paper(n-1) + 1
    else:
        return 2 * paper(n-1) - 1


T = int(input())
for tc in range(1, T + 1):
    # N은 10의 배수 중 한개
    N = int(input())
    print(f"#{tc} {paper(N//10)}")