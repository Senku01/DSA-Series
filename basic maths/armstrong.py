def armstrong(n):
    sum = 0 
    origin = n
    while (n> 0):
        ld = n % 10
        # amrstrong is **3 
        sum = sum + (ld**3)
        n= n//10
    if sum == origin:
        return "Armstrong" 
    else:
        return "Not a Armstrong"
    

n= int(input())
print(armstrong(n))