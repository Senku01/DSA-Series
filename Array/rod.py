def cutrod(arr):
    n= len(arr)
    for i in range(n):
        for j in range(i):
            print(arr[i+j])


arr=[1, 5 ,8, 9, 10, 17, 17, 20]

print(cutrod(arr) )