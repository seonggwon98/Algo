def find_dwarf(h):
    # 2^8 반복 하여 모든 부분 집합 생성
    for i in range(1 << n):
        # i번째 부분 집합 검사
        # i번째 부분 집합이 j번째 원소를 포함하고 있는지 확인
        seven = []
        for j in range(n):
            if i & (1 << j):
                seven.append(height[j])
                if len(seven) == 7:
                    sum_height = sum(seven)
                    if sum_height == 100:
                        return seven


# 난쟁이의 키가 9개 줄에 걸쳐 들어옴 연산이 필요하므로 int형으로 변환 후 받아줌
# 일곱 난쟁이의 키의 합 100
# 9개의 수로 만들 수 있는 부분 집합 중 길이가 7개인 부분 집합 중에 원소의 합이 100인 경우를 찾아 오름차순 정렬 후 출력
height = [0] * 9
n = 9
# 일단 입력 받아주고
for i in range(n):
    height[i] = int(input())
result = find_dwarf(height)
result.sort()
for i in result:
    print(i)
# 다른 풀이 난쟁이 9명의 키를 다 더하고 거기에서 100을 뺀 값 구해서
# 2 명의 합이 위의 값인 경우 그 두명을 뺀 나머지 출력