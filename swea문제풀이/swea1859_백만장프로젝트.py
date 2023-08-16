T = int(input())
for tc in range(1, T+1):
    days = int(input())
    prices = list(map(int, input().split()))
    # 최대값의 위치를 찾고 해당 위치까지 최댓값에서 해당 값들을 빼주며 이익에 더해준다
    # 최댓값의 위치 + 1 의 위치에서 부터 다시 시작하며 윗줄의 행동을 반복한다.
    # 최댓값까지 남은 날이 1 이상일 동안 반복해준다.
    benefit = 0
    while len(prices) > 0:
        max_p = max(prices)
        sell_index = prices.index(max_p)
        buy_prices = prices[:sell_index]
        # 남은 날 재 정의
        prices = prices[sell_index + 1:]
        for price in buy_prices:
            benefit += (max_p - price)
    print(f"#{tc} {benefit}")
