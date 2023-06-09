def insertion(arr):
    n= len(arr)
    for i in range(0, n-1):
        j= i 
        # Comparing till last element
        while( j>0 and arr[j-1]> arr[j] ):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1

my_list = [5, 2, 9, 1, 7, 1]
insertion(my_list)
print("Sorted list:", my_list)