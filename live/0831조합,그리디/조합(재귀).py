def comb(n, r):
    global count
    if r == 0:
        if sum(tr) == 0:
            count += 1
    elif n < r:
        return
    else:
        tr[r - 1] = arr[n - 1]
        comb(n - 1, r - 1)
        comb(n - 1, r)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
l = len(arr)
tr = [0] * l
count = 0
for i in range(l):
    comb(l, i)
print(count)