first = int(input())
# 3번째 수는 첫번째 수에서 2번째 수를 빼주어야 하므로
# 두번째 수는 첫 번째 수보다 작아야 한다.
max_len = 0
max_list =[]
for i in range(1, first + 2):
    second = i
    num_list = [first, second]
    next_idx = 2
    while True:
        if num_list[next_idx - 2] - num_list[next_idx - 1] >= 0:
            num_list += [0]
            num_list[next_idx] = num_list[next_idx - 2] - num_list[next_idx - 1]
            next_idx += 1
        else:
            break
    l = len(num_list)
    if max_len < l:
        max_len = l
        max_list = num_list[:]

print(max_len)
for j in range(max_len):
    print(max_list[j], end=" ")
