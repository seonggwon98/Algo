def max_(numbers):
    # 함수 호출시 변수 초기화
    max_num = 0
    max_index = 0
    for num in range(len(numbers)):
        if max_num < numbers[num]:
            max_num = numbers[num]
            max_index = num
    return max_index

def min_(numbers):
    # 함수 호출시 변수 초기화
    min_num = 1000
    min_index = 0
    for num in range(len(numbers)):
        if min_num > numbers[num]:
            min_num = numbers[num]
            min_index = num
    return min_index


T = 10
for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))
    for i in range(N):
        # 최댓값과 최솟값의 인덱스를 뽑아내어 각각 -1과 1씩 해준다.
        max_index = max_(boxes)
        min_index = min_(boxes)
         # 중간에 평탄화가 종료될 경우 덤프 반복을 종료 
        if boxes[max_index] - boxes[min_index] == 1 or 0:
            break
        # 평탄화 작업 계속 진행
        boxes[max_index] -= 1
        boxes[min_index] += 1
       
    # 위의 for문의 경우 N번 덤프 작업까지만 진행되었기 때문에
    # 그 후의 최댓값과 최솟값을 다시 한번 찾아준다. 
    max_index = max_(boxes)
    min_index = min_(boxes)
    print(f"#{tc} {boxes[max_index]-boxes[min_index]}")



# 정렬을 통해서 인덱스에 접근하여 푼 방법
# T = 10
# for tc in range(1, T + 1):
#     N = int(input())
#     boxes = list(map(int, input().split()))

#     for i in range(N): # N번 덤프 반복 수행
#         # 먼저 정렬을 하여 0번째와 -1번째가 각각 최소와 최대를 의미하므로
#         # 반복해서 최대값에서는 -1씩 최솟값은 +1씩 해주어 덤프를 표현
#         boxes.sort()
#         boxes[-1] -= 1
#         boxes[0] += 1
#         # 평탄화가 정해진 덤프 횟수보다 일찍 끝나는 경우는 최댓값과 최솟값이 최대 1 차이 나는 경우이므로 0과 1 중 한 값이 나오면 반복을 종료
#         if boxes[-1] - boxes[0] == 1 or 0:
#             break
#     # 마지막 덤프 반복 작업 후 정렬이 되어 있지 않기 때문에 한번 더 정렬 해 준 후 결과값 출력 
#     boxes.sort()
#     print(f"#{tc} {boxes[-1] - boxes[0]}")
