def find_duplicats(arr):
    seen = set()
    duplicate = set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    if len(duplicate) == 0:
        return -1
    return duplicate


arr= [ 2,3,1,2,3 ]

print(find_duplicats(arr))
    
