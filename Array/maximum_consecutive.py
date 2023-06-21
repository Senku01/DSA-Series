def maximum_once(arr):
    maxi =0 
    count = 0 
    for i in range(len(arr)):
        if arr[i]== 1:
            count +=1
            # maxi = max(maxi ,count)
        else:
            maxi = max(maxi,count)
            count = 0 
        maxi = max(maxi,count)
    return maxi
    # start=0
    # max1=0
    # c=0
    # for i in range(n):
    #     if arr[i]==0:
    #         c+=1
    #     while c>m:
    #         if arr[start]==0:
    #             c-=1
    #         start+=1
    #     max1=max(max1,i-start+1)
    # return max1

arr=[1, 0, 0, 1, 1, 0, 1, 0, 1, 1 ,1]

print(maximum_once(arr))