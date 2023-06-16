def rotate_array(arr, d):
    n = len(arr)
    temp = arr[:d]  # Copy the first D elements

    # Shift the remaining elements
    for i in range(d, n):
        arr[i - d] = arr[i]

    # Copy the elements from temp back into arr
    for i in range(n - d, n):
        arr[i] = temp[i - (n - d)]

    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotated_arr = rotate_array(arr, d)
print(rotated_arr)
