def isEmpty():
    return front == rear


def isFull():
    return rear == size - 1


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


T = int(input())
for tc in range(1, T + 1):
    # N : 숫자로 이루어진 배열 크기 M : 작업 반복 횟수
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # 총 queue의 크기는 numbers를 한번 입력해 주고 그 후에는 맨 앞의 요소를 dequeue
    # 해주어 해당 배열에 다시 enqueue 해주면 되므로 일단 숫자 배열 크기와 작업 반복 횟수를
    # 더한 값이 que의 전체 크기가 된다.
    # 해당 배열에서 M번 d
    size = N + M
    q = [0] * size
    front = rear = -1
    for i in range(N):
        enqueue(numbers[i])

    for j in range(M):
        x = dequeue()
        enqueue(x)

    print(f"#{tc} {dequeue()}")


