def selection(n,arr):
    for i in range(0,n-2):
        min = i 
        for j in range(i,n-1):
            if arr[j] < arr[min]:
                min = j
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr
    # def select(self, arr, i):
    #     # code here
    #     minIdx = i
    #     for idx in range(i+1, len(arr)):
    #         if arr[minIdx] > arr[idx]:
    #             minIdx = idx
        
    #     return minIdx
            
    
    # def selectionSort(self, arr,n):
    #     #code here
    #     for i in range(n):
    #         idx = self.select(arr,i)
    #         arr[i], arr[idx] = arr[idx], arr[i]
            
    #     return arr

n= 5
arr = [4,1,3,9,7]
print(arr)

sortedarr = selection(n, arr)

for i in range(len(sortedarr)):
    print(sortedarr[i], end=' ')

