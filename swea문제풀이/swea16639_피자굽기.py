# 삽입 연산
def enqueue(item):
    global rear
    # 삽입을 하기 전에 큐가 가득 찼는지 확인
    if isFull():
        print("full")
        return
    rear += 1
    q[rear] = item


# 삭제 연산
def dequeue():
    global front
    # 삭제 하기 전에 큐가 비어있는지 확인
    if isEmpty():
        print("empty")
        return
    front += 1
    return q[front]


# 큐가 가득 찼는지
def isFull():
    return rear == size - 1


# 큐가 비어있는지
def isEmpty():
    return front == rear


T = int(input())
for tc in range(1, T + 1):
    # N : 화덕의 크기 M : 피자 개수
    N, M = map(int, input().split())
    cheezes = list(map(int, input().split()))
    size = 30 * M
    q = [0] * size
    front = rear = -1
    # 치즈의 양에 따라 녹는 시간이 다르다 즉 꺼내지는 순서는 다를 수 있음
    # 피자는 1번 위치 뺄 수 있음
    # 잠시 꺼내고 같은 자리에 넣을 수 있다
    # 한바퀴 돌 때 녹지 않은 치즈의 양은 반으로 즉 다시 꺼냈을 때 치즈 양 절반
    # 일단 순서대로 화덕의 크기만큼 피자를 넣고
    dic_cheeze = {}
    for i in range(1, M + 1):
        dic_cheeze[i] = cheezes[i - 1]

    for i in range(1, N + 1):
        enqueue(i)
    # 처음 오븐에 넣었던 마지막 피자 번호가 i라고 했을 때 다음에 넣어줄 피자번호를 저장
    next_pizza = i + 1
    while True:
        # 오븐이 비었다면 종료
        if isEmpty():
            break
        # 처음 넣었던 피자 번호 dequeue()
        pizza_num = dequeue()
        # 해당 피자 번호의 치즈가 다 녹은 상태로 변경
        dic_cheeze[pizza_num] //= 2
        # 치즈가 다 녹았는지 확인
        check = dic_cheeze[pizza_num]
        if check == 0:
            # 화덕 안에 있던 피자가 다 구워 졌다면 다음 번호의 피자를 큐에 넣어주어야하고
            # 넣고 난 후는 다음 피자 번호를 1 증가 시켜주어야 한다.
            # 다음 피자 번호가 주어진 피자 번호들 보다 크다면 동작 하지 X 조건 걸어주어야함
            if next_pizza <= M:
                enqueue(next_pizza)
                next_pizza += 1
            # 화덕 안의 피자 중 아직 제대로 구워진 것이 없다면 while문 초반에 꺼냈던 번호의 피자를
            # queue 배열의 뒤로 넣어준다.
        else:
            enqueue(pizza_num)

    print(f"#{tc} {pizza_num}")
