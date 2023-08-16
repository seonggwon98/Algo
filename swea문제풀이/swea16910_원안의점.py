T = int(input())

for tc in range(1, T+1):
    N = int(input())
    count = 0
    for x in range(N+1,-N-1,-1):
        for y in range(N+1, -N-1,-1):
            if x**2 + y**2 <= N**2:
                count += 1
    print(f"#{tc} {count}")