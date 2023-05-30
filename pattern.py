## Patters:
## for the outer loop, count the no of rows
## for the inner loop, focus on the colums,
## & connect them somehow to the rows
## print them "*" inside the inner for loop
## observe symmentry [optional]

def patter1(n):
    for i in range(n):
        for j in range(n):
            print('*', end='')
        print()
    # *********
    # *********
    # *********
    # *********
    # *********
    # *********
    # *********
    # *********
    # *********

def patter2(n):
    for i in range(1, n+1):
        for j in range(i):
            print ('*', end='')
        print()
        # 3
        # *
        # **
        # ***


def patter3(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(j , end=' ')
        print()
        #4
        # 1 
        # 1 2 
        # 1 2 3 
def patter4(n):
    for i in range(1,n+1):
        for j in range(1,i):
            print(i , end=' ')
        print()
        #4
        # 1 
        # 2 2 
        # 3 3 3 
       
def patter5(n):
    for i in range(1,n+1):
        ##formula to calculate n-row+1
        for j in range(n-i+1):
            print('* ', end='')
        print()
        #5
        # * * * * * 
        # * * * * 
        # * * * 
        # * * 
        # * 

def patter6(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            print(j, end=' ')
        print()
        #5
        # 1 2 3 4 5 
        # 1 2 3 4 
        # 1 2 3 
        # 1 2 
        # 1 


def pattern7(n):
    for i in range(0,n+1):
        for j in range(0,n-i-1):
            print(" ", end='')
            for k in range(0,2*i+1):
                print("* ", end='')
                print(" ", end='')
            print()

n=int(input())
pattern7(n)