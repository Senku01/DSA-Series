def check_sorted(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return 0
    return 1

arr=[10, 20, 30, 40 ,50 ]
print(check_sorted(arr))