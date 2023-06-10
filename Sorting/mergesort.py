def merge(arr, low , mid ,high):
    ar = []
    left = low
    right = mid+1
    while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
            ar.append(arr[left])
            left +=1
        else:
            ar.append(arr[right])
            right+=1
    while(left <= right):
        ar.append(arr[left])
        left+=1
    while(right <= left):
        ar.append(arr[right])
        right+=1
    for i in range(low , high+1):
        arr[i] = ar[i-low] 

def mergesort(arr,low ,high):
    if (low >= high): return  
    mid = (low + high) //2
    mergesort(arr , low , mid)
    mergesort(arr , mid+1 , high)
    merge(arr ,low , mid , high)