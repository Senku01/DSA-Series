arr=[3,2,1,51,2]
def largest_of_array(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if (arr[i] > largest):
            largest = arr[i]
            return largest

print(largest_of_array(arr))


print("Lenght:" ,len(arr))