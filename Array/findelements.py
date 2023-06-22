def find_elements(arr):
    mp = {}
    for num in arr:
        if num in mp:
            mp[num ]+=1
        else:
            mp[num] =1
    
    for num,count in mp.items():
        if count == 1:
            return num 
    return -1

arr= [2, 2, 5, 5, 20, 30, 30]

print(find_elements(arr))