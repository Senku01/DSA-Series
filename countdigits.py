
## if the problem have division the TC will be in Log only 

def count(n):
    nlen = len(str(n))
    strn  = str(n)
    count =0 
    for i in range(nlen):
        d = int(strn[i])
        if d !=0:
            if n % d ==0:
                count +=1
    return count

n= int(input())
print(count(n))