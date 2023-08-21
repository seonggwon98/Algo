def inorder(t):
    # 왼쪽
    inorder(child_left[t + 1])
    t = t
    # 오른쪽
    inorder(child_right[t + 2])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    child_left = [0] * (N + 1)
    child_right = [0] * (N + 1)
    num = 1
    for i in range(1, N + 1):
        parent = i * 2
        child = i * 2 + 1
        if child_left[parent] == 0:
            child_left[parent] = child
        else:
            child_right[parent] = child
    inorder(1)

