T = int(input())
for tc in range(1, T + 1):
    cn, N = input().split()
    N = int(N)
    str_arr = list(input().split())
    # 해당 인덱스와 대응되는 문자 배열
    numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 카운트 배열과 결과 배열을 만들어줌
    count = [0] * 10
    new_arr = [0] * (N + 1)
    for i in range(N):
        for j in range(10):
            if str_arr[i] == numbers[j]:
                count[j] += 1
    # 갯수가 파악된 카운트 배열에서 자리 찾기를 위한 배열을 만들기 위해 i번째에 i-1번째 수를 더해주어 새로운 카운트 배열 생성
    for n in range(1, 10):
        count[n] += count[n - 1]
    # 안정 정렬을 위해 뒤에서부터 차근 차근 해당 자리에 알맞은 값을 넣는다
    for k in range(N - 1, -1, -1):
        for p in range(10):
            if str_arr[k] == numbers[p]:
                count[p] -= 1
                new_arr[count[p]] = numbers[p]
    print(cn)
    print(*new_arr)
