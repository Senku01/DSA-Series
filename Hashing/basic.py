# TC -> O(N) ff

# def f(n, a):
#     cut =0 
#     for i in range(n):
#         if a[i] == n:
#             cut +=1
#     return cut 


#TC -> O(N*N)
#SC -> O(N)

def countfreq(arr,n):
    # mp ={}
    # for i in range(n):
    #     if arr[i] in mp:
    #         mp[arr[i]] +=1
    #     else:
    #         mp[arr[i]] = 1
    # for i in range(1,n+1):
    #     if i in mp:
    #         print(mp[i],end=' ')
    #     else:
    #         print(0, end='-')
    mp={}
    for x in arr:
        mp[x]=mp.get(x,0)+1
    for i in range(n):
        arr[i]=mp.get(i+1,0)

def repeat(arr ,n):
    fre = {}
    max_freq = 0
    mos_fre_ele = None
    for i in range(n):
        if arr[i] in fre:
            fre[arr[i]] +=1
        else:
            fre[arr[i]] = 1
        if fre[arr[i]] > max_freq:
            max_freq = fre[arr[i]]
            mos_fre_ele = arr[i]
    return mos_fre_ele 

arr = [1, 2, 3, 4]
n= len(arr)
print(repeat(arr,n))

