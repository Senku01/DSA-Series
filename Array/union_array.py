def union(arr1,arr2):
    # if we use set it generally eliminates the duplicates
    # from the array 
    set1 = set(arr1)
    set2 = set(arr2)

    union_set = set1 | set2
    union_list = sorted(union_set)

    return union_list

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]

print(union(arr1, arr2))