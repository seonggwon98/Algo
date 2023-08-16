def count_search(page, Na):
    start = 1
    end = page
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == Na:
            break
        elif middle > Na:
            end = middle 
        else:
            start = middle

    return count
T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())  # P는 전체 페이지 A는 A가 찾아야할 페이지 B는 B가 찾아야할 페이지
    count_a = count_search(P, A)
    count_b = count_search(P, B)
    if count_a < count_b:
        result = 'A'
    elif count_a > count_b:
        result = 'B'
    else:
        result = 0
    print(f"#{tc} {result}")
