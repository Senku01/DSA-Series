# find Factorial Number or not 
def fact(n):
    x =1
    facto =1
    while facto < n:
        x +=1
        facto *=x
    if facto == n:
        return 1
    else:
        return 0

# Find all factorial num

def ffact(n):
    fac = 1 
    x = 2 
    ans = []
    while fac <= n:
        ans.append(fac)
        fac *= x 
        x += 1 
    return ans

n=int(input())
print(fact(n))

