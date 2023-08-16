def rsp_game(x, y):
    if x == y:
        return "비김"
    elif x == 1 and y == 3:
        return "X"
    elif x == 3 and y == 1:
        return "Y"
    elif x > y:
        return "X"
    else:
        return "Y"

# 재귀
def tournament(i, j):
    if i == j:
        return i
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2+1, j)
        game = rsp_game(cards[left], cards[right])
        if game == "비김":
            return left
        elif game == "X":
            return left
        elif game == "Y":
            return right


T = int(input())
for tc in range(1, T + 1):
    # 인원수 N과 고른 카드가 번호순으로 주어짐
    N = int(input())
    cards = list(map(int, input().split()))
    # 가위 : 1 바위 : 2 보 : 3
    winner = tournament(0, N - 1)
    print(f"#{tc} {winner+1}")