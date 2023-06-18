def linear_search(k ,arr):
    n= len(arr)
    for i in range(0,n):
        if arr[i] == k:
            return i
    return -1
k=6    
arr=[1,2,3,4,6]

print(linear_search(k,arr))