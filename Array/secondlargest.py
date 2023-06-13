def secondlargest(arr):
    # largest = float('-inf')
    # second_largest = float('-inf')

    # for i in arr:
    #     if  i > largest:
    #         second_largest = largest
    #         largest = i 
    #     elif i > second_largest:
    #         second_largest = i 
    # return seond_largest
    n= len(arr)
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    if second_large == float('-inf'):
        return -1
    else:
        return second_large

arr = [642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642, 642]
print(secondlargest(arr))