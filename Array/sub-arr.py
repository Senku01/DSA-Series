def sub_arr(arr,k):
    n= len(arr)
    left ,right =0 , 0
    sum = arr[0]
    maxlen = 0
    while right <n :
        while left<= right and sum >k:
            sum -= arr[left]
            left +=1
        if sum == k:
            maxlen = max(maxlen ,right-left +1)
        right +=1
        if right <n : sum +=arr[right]
    return maxlen

k= 6
arr=[ -1, 2, 3]
print(sub_arr(arr,k))

