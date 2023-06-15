def rotate_left(arr,k):
    # n= len(arr)
    # temp = arr[0]
    # for i in range(1, n):
    #     arr[i-1] = arr[i]
    # arr[n-1] = temp 
    # return arr
    n= len(arr)
    k = k % n
    temp = arr[:k]
    for i in range(n- k):
        arr[i]= arr[i+k]
    arr[n-k] = temp
    return arr    
    # n= len(arr)
    # k =k % n
    # arr = arr[k:] + arr[:k]
    # return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(rotate_left(arr,2))