def even_odd(arr):
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    if even_index == len(arr):
        return 1
    else:
        return 0

arr = [3, 6, 12, 1, 5, 8]
print(even_odd(arr))