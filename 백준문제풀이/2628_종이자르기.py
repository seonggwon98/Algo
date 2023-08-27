W, L = map(int, input().split())
cut = int(input())
width, length = [0, L], [0, W]
cut_list = [list(map(int, input().split())) for _ in range(cut)]
# 먼저 컷 정보 저장
for i in range(cut):
    if cut_list[i][0] == 0:
        width.append(cut_list[i][1])
    else:
        length.append(cut_list[i][1])
# 정렬 후 가로 와 세로 각각 원소들끼리의 차를 이용해서 최대 값을 얻는다
width.sort()
length.sort()
max_w = max_l = 0
for i in range(1, len(width)):
    tmp = width[i] - width[i - 1]
    if max_w < tmp:
        max_w = tmp
for j in range(1, len(length)):
    tmp = length[j] - length[j - 1]
    if max_l < tmp:
        max_l = tmp
print(max_w * max_l)
