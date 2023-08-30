def selection_sort(i, n):
    if i == n:
        return
    else:
        # remain = arr[i:]
        # idx = remain.index(min(remain)) + i
        # arr[i], arr[idx] = arr[idx], arr[i]
        # selection_sort(i + 1, n)
        min_i = i
        for j in range(i + 1, n):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
        selection_sort(i + 1, n)


arr = [5, 1, 4, 2, 3, 6, 5, 4, 3, 2]
N = 10
selection_sort(0, N)
print(arr)