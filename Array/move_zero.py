def move_zero(arr):
    # n= len(arr)
    # j= -1 
    # for i in range(0,n):
    #     if arr[i] == 0:
    #         j= i 
    #         break
    # for i in range(j+1,n):
    #     if arr[i] != 0:
    #         temp = arr[i]
    #         arr[i]= arr[j]
    #         arr[j] = temp 
    #         j+=1
    # return arr

    n = len(arr)
    j = -1
    for i in range(n):
        if arr[i] != 0:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    return arr

arr =[3, 5, 0, 0, 4]
print(move_zero(arr))
