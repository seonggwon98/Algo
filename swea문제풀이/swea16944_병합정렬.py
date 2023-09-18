def merge(left, right):
    result = []
    lenl = len(left)
    lenr = len(right)
    lrear = rrear = 0
    # 좌우 둘 다 비어있는 리스트가 될 때 까지 합친다
    while lenl > 0 or lenr > 0:
        if lenl > 0 and lenr > 0:
            if left[lrear] <= right[rrear]:
                result.append(left[lrear])
                lrear += 1
                lenl -= 1
            else:
                result.append(right[rrear])
                rrear += 1
                lenr -= 1
        elif lenl > 0:
            result.append(left[lrear])
            lrear += 1
            lenl -= 1
        elif lenr > 0:
            result.append(right[rrear])
            rrear += 1
            lenr -= 1
    return result


def merge_sort(arr):
    global count
    m = len(arr)
    # 종료 조건 나눌 수 없을 때 까지
    if m == 1:
        return arr
    left = right = []
    middle = m // 2
    left, right = arr[:middle], arr[middle:]
    # 정복
    left = merge_sort(left)
    right = merge_sort(right)

    if left[-1] > right[-1]:
        count += 1

    return merge(left, right)


T = int(input())
for tc in range(1, T + 1):
    count = 0
    N = int(input())
    li = list(map(int, input().split()))
    X = merge_sort(li)
    print(f"#{tc} {X[N // 2]} {count} ")
