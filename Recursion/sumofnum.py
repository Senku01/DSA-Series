# Sum of First n terms
def sum (n):

    # if n < 1 or n >1000:
    #     return 
    # if (n == 0):
    #     return 0
    # return pow(n,3) + sum(n-1)
    sum = n * (n+1)//2
    return sum* sum


# TC -> O(n)
# SC -> O(n)
# Factorial
def fact(n):
    if (n == 0):
        return 1 
    return n * fact(n-1)

n= int(input())
print(fact(n))
