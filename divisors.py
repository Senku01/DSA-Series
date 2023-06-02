
#TC = O(n)
#SC = O(1)
def divisor(n):
    sum =0
    i=1
    while(i<=n):
        sum+= ((n//i)*i)
        i+=1
    return sum

n= int(input())
print(divisor(n))    