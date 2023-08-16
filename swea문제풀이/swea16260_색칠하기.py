T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N은 칠할 영역의 개수
    info_arr = [list(map(int, input().split())) for _ in range(N)]
    
    # 0으로 이루어진 10 * 10의 배열을 만들어 줌 
    zeros_arr = [[0] * 10 for _ in range(10)]
    count_ = 0
    # 색을 칠할 영역의 수만큼 반복
    for i in range(N):
        # 입력된 정보에서 칠할 색의 숫자와 색을 칠할 행과 열의 정보를 찾아 저장
        start_row = info_arr[i][0]
        end_row = info_arr[i][2]
        start_col = info_arr[i][1]
        end_col = info_arr[i][3]
        color = info_arr[i][4]
        # 0으로 만들어둔 판에 위의 반복에서 찾은 정보를 바탕으로 색을 칠한다(색의 값을 더해줌)
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                zeros_arr[r][c] += color
    # 색이 다 칠해진 판에서 보라색(3)을 찾아 카운트 해준다.            
    for z_r in range(10):
        for z_c in range(10):
            if zeros_arr[z_r][z_c] == 3:
                count_ += 1
    print(f"#{tc} {count_}")
