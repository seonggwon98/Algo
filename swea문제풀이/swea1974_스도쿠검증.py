def is_sudoku(arr):
    if len(set(arr)) == 9:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    # 일단 행이 스도쿠 인지 확인
    # 그 후에 열 우선 순회를 통해 스도쿠 확인
    # 그리고 각 3*3 배열을 돌면서 제대로 된 스도쿠 확인
    # 제대로 된 스도쿠 확인은 해당 행 이나 열이나 배열을 집합으로 저장 했을 때
    # 크기가 9가 아니라면 제대로 된 스도쿠가 아니다
    sudoku_check = 0
    last_check = 1
    for i in range(9):
        sudoku_check = is_sudoku(sudoku[i])
        if sudoku_check == 0:
            last_check = 0
    for i in range(9):
        sudoku_c = []
        for j in range(9):
            sudoku_c.append(sudoku[j][i])
        sudoku_check = is_sudoku(sudoku_c)
        if sudoku_check == 0:
            last_check = 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sudoku_arr = []
            for k in range(3):
                for p in range(3):
                    sudoku_arr.append(sudoku[i+k][j+p])
            sudoku_check = is_sudoku(sudoku_arr)
            if sudoku_check == 0:
                last_check = 0
    print(f"#{tc} {last_check}")

