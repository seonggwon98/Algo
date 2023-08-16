T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()
    max_string = ''
    max_count = 0
    for i in range(len(N)):
        count = 0
        for j in range(len(M)):
            if N[i] == M[j]:
                count +=1
        if max_count < count:
            max_count = count
            max_string = N[i]
    print(f"#{tc} {max_count}")
            
