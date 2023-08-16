T = 10
for tc in range(1, T + 1):
    N = int(input()) # 건물의 개수
    buildings = list(map(int, input().split()))
    # 처음과 끝은 2칸씩 비어져 있으므로 범위를 설정한다.
    count = 0
    for i in range(2, N - 2):
        # 해당 건물의 꼭대기 층에서부터 카운트 해가며 양옆 2칸을 비교하며
        # 조망권에 영향을 받는지 확인한후 조망권 층을 1씩 증가
        for j in range(buildings[i], -1, -1):
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]: 
                count += 1
            else:
                break
    print(f"#{tc} {count}")
ss