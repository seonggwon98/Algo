# import sys
# sys.stdin = open("input.txt","r")
# T개 의 테스트 케이스에 대한 반복
T = int(input())
# 필요한 정보 변수로 저장
ground, brick, steel, water = '.', '*', '#', '-'
lookup, lookdown, lookleft, lookright = '^', 'v', '<', '>'
up, down, left, right, shoot = 'U', 'D', 'L', 'R', 'S' 

for tc in range(1, T + 1):
    h, w = map(int, input().split())  # H = 높이  W = 너비 공백 기준으로 받아줌
    game_map = [list(input()) for _ in range(h)] # H개의 길이가 W인 문자열이 공백없이 주어진다.
    n = int(input()) # 사용자 입력 즉 게임 진행 입력 개수가 주어진다.
    user_input = list(input()) # 길이가 N 개인 문자열이 공백없이 주어진다
    # 먼저 해당 전차의 첫 위치를 찾는다.
    # 전차의 위치를 저장 하고 사용자의 입력에 따라 움직이게 반복
    # 전차의 전진 방향과 방향에 따라 움직일 상태를 정하고 평지라면 이동 아니라면 변화 없음
    # S 명령의 경우 포탄 발사 포탄의 경우 전차가 바라보고 있는 쪽의 다음 칸을 확인하며 벽 유무 파악 벽돌일 시 부딫히고 해당 땅 평지로 강철은 폭탄만 파괴 맵 밖은 변화 없음
    
    # 방향을 정하기 위한 델타 배열 생성
    # 0 = 하 1 = 상 2= 좌 3= 우 
    dr = [1, -1, 0, 0]
    dc = [0 , 0, -1, 1] 
    # 해당 전차의 위치를 찾기 위해 맵을 돌며 위치 정보 저장 맵 사이즈는 H*W 
    for i in range(h):
        for j in range(w):
            # if문을 통해 전차 발견시 해당 전차의 위치와 상태를 저장
            if game_map[i][j] == lookup or game_map[i][j] == lookdown or game_map[i][j] == lookleft or game_map[i][j] == lookright:
                start_r = i
                start_c = j
                state = game_map[i][j]
    
    # 입력에 따른 반복 시작
    for inp in user_input:
        # input에 따라 5가지 상황 존재 up, down, left, right, shoot
        if inp == up:
            # 전차의 방향을 변경해주고 다음 위치로 이동 가능한지 여부를 파악 후 평지라면 이동
            # up이므로 바로 위의 위치를 확인
            state = lookup
            game_map[start_r][start_c] = state
            nr = start_r + dr[1]
            # 변경할 위치가 맵의 범위 안인지 확인 그 후 땅 확인 후 이동 땅은 전차의 상태를 값으로 가짐
            # 지나온 땅은 다시 평지로 변경 변경한 위치를 시작 지점으로 변경
            if 0 <= nr < h and 0 <= start_c < w:
                if game_map[nr][start_c] == ground:
                    game_map[start_r][start_c] = ground
                    game_map[nr][start_c] = state
                    start_r = nr
                else:
                    # 벽이나 물일 경우 현재 위치에 전차의 상태 값 저장
                    game_map[start_r][start_c] = state
        # 방향 관련 나머지 경우는 up과 유사
        elif inp == down:
            state = lookdown
            game_map[start_r][start_c] = state
            nr = start_r + dr[0]
            if 0 <= nr < h and 0 <= start_c < w:
                if game_map[nr][start_c] == ground:
                    game_map[start_r][start_c] = ground
                    game_map[nr][start_c] = state
                    start_r = nr
                else:
                    # 벽이나 물일 경우 현재 위치에 전차의 상태 값 저장
                    game_map[start_r][start_c] = state
        elif inp == left:
            state = lookleft
            game_map[start_r][start_c] = state
            nc = start_c + dc[2]
            if 0 <= start_r < h and 0 <= nc < w:
                if game_map[start_r][nc] == ground:
                    game_map[start_r][start_c] = ground
                    game_map[start_r][nc] = state
                    start_c = nc
                else:
                    # 벽이나 물일 경우 현재 위치에 전차의 상태 값 저장
                    game_map[start_r][start_c] = state
        elif inp == right:
            state = lookright
            game_map[start_r][start_c] = state
            nc = start_c + dc[3]
            if 0 <= start_r < h and 0 <= nc < w:
                if game_map[start_r][nc] == ground:
                    game_map[start_r][start_c] = ground
                    game_map[start_r][nc] = state
                    start_c = nc
                else:
                    # 벽이나 물일 경우 현재 위치에 전차의 상태 값 저장
                    game_map[start_r][start_c] = state
        # 마지막 경우는 S 경우
        # 전차가 바라보는 방향을 확인하고 해당 방향으로 폭탄이 사라질 때까지 전진
        else :
            cannon_dir = state
            cannon_r = start_r
            cannon_c = start_c
            cannon = 1
            # 포탄이 멈출 때 까지 계속 진행
            while cannon == 1:
                # 포탄의 방향 먼저 확인
                if cannon_dir == lookup:
                    # 포탄의 방향에 맞춰서 1칸 씩 이동     
                    cannon_r -= 1 
                    # 포탄이 범위 안에서만 있게 
                    if 0 <= cannon_r < h and 0 <= cannon_c < w:
                        # 벽돌을 만날 경우 해당 위치 평지로 변경 포탄 소멸 강철은 그냥 포탄 소멸
                        if game_map[cannon_r][cannon_c] == brick:
                            game_map[cannon_r][cannon_c] = ground
                            cannon = 0
                        elif game_map[cannon_r][cannon_c] == steel:
                            cannon = 0 
                    # 범위 밖으로 나갔을 시 포탄 소멸
                    else:
                        cannon = 0
                elif cannon_dir == lookdown:
                    cannon_r += 1 
                    if 0 <= cannon_r < h and 0 <= cannon_c < w:
                        if game_map[cannon_r][cannon_c] == brick:
                            game_map[cannon_r][cannon_c] = ground
                            cannon = 0
                        elif game_map[cannon_r][cannon_c] == steel:
                            cannon = 0 
                    else:
                        cannon = 0
                elif cannon_dir == lookleft:
                    cannon_c -= 1 
                    if 0 <= cannon_r < h and 0 <= cannon_c < w:
                        if game_map[cannon_r][cannon_c] == brick:
                            game_map[cannon_r][cannon_c] = ground
                            cannon = 0
                        elif game_map[cannon_r][cannon_c] == steel:
                            cannon = 0 
                    else:
                        cannon = 0 
                elif cannon_dir == lookright:
                    cannon_c += 1 
                    if 0 <= cannon_r < h and 0 <= cannon_c < w:
                        if game_map[cannon_r][cannon_c] == brick:
                            game_map[cannon_r][cannon_c] = ground
                            cannon = 0
                        elif game_map[cannon_r][cannon_c] == steel:
                            cannon = 0 
                    else:
                        cannon = 0
                else:
                    cannon = 0 
                                          
    print(f"#{tc}", end =' ')
    for s in range(h):    
        print(''.join(game_map[s]))
