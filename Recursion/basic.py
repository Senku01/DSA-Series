def printname(i,n):
    if (i>n):
        return 
    print("Vignesh")
    printname(i+1,n)
    
# Print name linerally from 1 to N
def linear_name(i,n):
    if(i>n):
        return 
    print("Vignesh")
    linear_name(i+1,n)

# PRint in terms of N to 1 in opposite fashion
def n_name(i,n):
    if (i<1):
        return
    print(i)
    n_name(i-1,n)

#


n= int(input())
n_name(n,n)