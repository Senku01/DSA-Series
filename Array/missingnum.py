def missing(arr,n):
    hash = [0] *(n+1)

    for i in range(n-1):
        hash[arr[i]] +=1
    
    for i in range(1, n+1):
        if hash[i] == 0:
            return i 
    
    return -1 

n= 4
arr=[1, 4, 3]

print(missing(arr,n))

