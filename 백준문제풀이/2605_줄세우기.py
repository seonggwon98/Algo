# N : 학생 수
N = int(input())
# arr : 학생들이 뽑은 번호
arr = list(map(int, input().split()))
# 학생들 일단 한줄로 세우기
student = list(range(1, N + 1))
for i in range(N):
    # 해당 값이 0이 아니라면 교환을 해주어야 함
    # 해당 위치에서 옮겨야할 숫자만큼 빼준 위치까지 i와 i-1번째를 교환해 가면서 줄을 선다
    if arr[i] != 0:
        for j in range(i, i - arr[i], -1):
            student[j], student[j - 1] = student[j - 1], student[j]
print(*student)
