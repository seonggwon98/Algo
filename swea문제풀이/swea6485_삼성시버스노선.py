# 첫 입력은 테스트 케이스의 수
T = int(input())
for tc in range(1, T + 1):
    # 하나의 정수 N이 주어 지고
    # 그 밑으로  N개의 줄에 Ai 와 Bi가 공백을 기준으로 주어지므로 N번 반복
    N = int(input())
    # A, B를 저장 AB 리스트 생성
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))  # N번째 노선의 A 이상 B 이하인 모든 정류장을 다니는 노선
    P = int(input())  # P는 P개의 버스 정류장
    # P개의 반복을 하면서 C값을 받아주며 구해야할 정류장 번호를 리스트로 받아준다
    # 리스트 컴프리헨션으로 표현  C = [int(input()) for _ in range(P)] (for 앞에 받는 자료를 리스트로 만들어준다)
    C = []
    for j in range(P):
        C.append(int(input()))  # C는 지나는 노선의 갯수가 몇개인지 구해야할 버스 정류장의 번호가 주어진다.
    # 처음으로 N 번째 노선이 지나는 버스 정류장의 갯수를 카운팅 해준다
    # 카운팅 해줄 배열을 만든다 1 부터 5000번 까지 번호가 존재하므로 5001개의 0으로 된 배열을 만들어 준다
    bus_stop_numbers = [0] * 5001
    # AB에서 언패킹을 통해 A이상 B이하의 정류장에 카운트를 통해 각 정류장에 몇 개의 노선이 지나갔는지 확인 가능
    for A, B in AB:
        for bus_stop in range(A, B + 1):
            bus_stop_numbers[bus_stop] += 1
    print(f"#{tc}", end = ' ')
    for k in C:
        print(bus_stop_numbers[k], end=' ')
    # 출력이 끝난 후 줄 바꿈 진행해 주어야 다음 테스트 케이스의 출력이 제대로 나옴
    print()

