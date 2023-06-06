def max_frequency(nums,k):
    mp ={}
    max_fre = 0
    for num in nums:
        if num not in mp:
            mp[num] =1
        else:
            mp[num] +=1
        max_fre= max(max_fre , mp[num])
    sorted_num = sorted(set(nums))
    for i in range(1, len(sorted_num)):
        num =sorted_num
        ops_needed = (num - sorted_num[i-1]) * mp[sorted_num[i-1]]
        if ops_needed <=k:
            max_fre = max(max_fre, mp[num] * (ops_needed // (num - sorted_num[i-1]))) 
            k -= ops_needed
        else:
            break
    return max_fre

nums =[1,2,4]
k=5
max_frequency(nums,k)