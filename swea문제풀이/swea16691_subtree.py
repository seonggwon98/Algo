def preorder(t):
    if t:
        # t에서 방문처리
        global count
        count += 1
        # 왼쪽
        preorder(child_left[t])
        # 오른쪽
        preorder(child_right[t])
        return count


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    child_left = [0] * (E + 2)
    child_right = [0] * (E + 2)
    count = 0
    # 인덱스 번호가 부모 노드인 경우
    for i in range(E):
        parent = pairs[i * 2]
        child = pairs[i * 2 + 1]
        if child_left[parent] == 0:
            child_left[parent] = child
        else:
            child_right[parent] = child
    print(f"#{tc} {preorder(N)}")
