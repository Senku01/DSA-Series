import sys
n=int(input())

def reverse(n):
    sign = -1 if n<0 else 1
    n = abs(n) 
    revnum = 0 
    while (n>0):
        ld = n % 10 
        revnum = (revnum *10) + ld
        n = n //10 
    reverses = revnum * sign
    if reverses > 2147483647 or reverses < -2147483647:
        return 0
    else:
        return reverses
print(reverse(n))