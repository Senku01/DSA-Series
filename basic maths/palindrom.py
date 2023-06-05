def palindrom(n):
    if n < 0:
        n = abs(n)
    reverse = 0
    origi = n
    while (n>0):
        ld = n % 10
        reverse = (reverse *10) + ld
        n= n //10
    if str(reverse) == str(origi):
        return 'true'
    else:
        return 'false'

n=  int(input())

print(palindrom(n))