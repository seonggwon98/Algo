def make_tree(t):
    global num
    if t > N:
        return
    make_tree(2 * t)
    tree[t] = num
    num += 1
    make_tree(2 * t + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1
    make_tree(1)
    print(f"#{tc} {tree[1]} {tree[N//2]}")
