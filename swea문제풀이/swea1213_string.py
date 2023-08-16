T = 10
for i in range(1, T + 1):
    tc = int(input())
    pattern = input()
    text = input()
    pi = 0
    ti = 0
    count_p = 0
    count = 0
    # 주어진 text 문자열의 끝까지 진행한다.
    while ti < len(text):
        if text[ti] == pattern[pi]:
            pi += 1
            ti += 1
            count_p += 1
            # 계속 검사가 진행되어 해당 패턴 발견시 패턴의 인덱스는 패턴의 처음으로 돌아가고 개수는 증가
            if count_p == len(pattern):
                pi = 0
                count_p = 0
                count += 1
        else:
            count_p = 0
            ti = ti - pi + 1
            pi = 0
    print(f"#{tc} {count}")
