T = 10
for tc in range(1, T+1):
    N, M = input().split()
    N = int(N)
    M = list(M)
    password = []
    for i in range(N):
        password.append(M[i])
        if len(password) < 2:
            continue
        # 삽입된 숫자가 같은 숫자라면 전에 있는 숫자까지 빼준다.
        else:
            if password[-1] == password[-2]:
                for j in range(2):
                    password.pop()
    print(f"#{tc} ", end="")
    print(''.join(password))