T = int(input())
for tc in range(1, T + 1):
    # 문자열 M 안에 N과 일치하는 부분이 있는지 확인
    N = input()
    M = input()
    ni = 0
    mi = 0
    answer = 0
    while mi < len(M) and ni < len(N):

        if M[mi] == N[ni]:
            mi += 1
            ni += 1
        else:
            mi = mi - ni + 1
            ni = 0
            
        if ni == len(N):
            answer = 1
            break
    print(f"#{tc} {answer}")
