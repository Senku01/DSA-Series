def remove_duplicate(arr):
    arr.sort()
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return arr[:i + 1]


arr= [2, 2, 2, 2, 2]
print(remove_duplicate(arr))