def prime(n):
    count =0 
    if n <2:
        print("Not Prime")
    for i in range(2,int(n ** 0.5)+1):
        if n % i ==0:
            count +=1
            break
    if count ==0:
        return "Prime"
    else:
        return "Not Prime"

n= int(input())
print(prime(n))