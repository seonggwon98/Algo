T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    # 카운팅을 통해 가장 많이 카드에 적힌 숫자가 무엇인지 파악
    # 카운트 배열을 생성 
    count_arr = [0]*10
    # numbers를 순회하며 해당 값을 count_arr 인덱스에서 1씩 증가
    for number in numbers:
        count_arr[number] += 1
    # 카운트 횟수가 같을 때 숫자가 큰 쪽을 출력하기 때문에 인덱스
    # 거꾸로 확인하며 체크
    max_count = 0
    for i in range(len(count_arr) - 1, -1, -1):
        if max_count < count_arr[i]:
            max_count = count_arr[i]
            max_index = i
    print(f"#{tc} {max_index} {max_count}")
        
