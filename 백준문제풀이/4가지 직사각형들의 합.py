arr = [[0] * 101 for _ in range(101)]

for i in range(4):
    sr, sc, er, ec = map(int, input().split())
    for r in range(sr, er):
        for c in range(sc, ec):
            arr[r][c] = 1

count = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            count += 1

print(count)
