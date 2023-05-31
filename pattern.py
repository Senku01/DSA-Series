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
    for i in range(n):
        #Space
        for j in range(n-i+1):
            print(" ",end="")
        #Star 
        for j in range(2*i+1):
            print("*", end="")
        #Space
        for j in range(n-i+1):
            print(" ",end="")
        print()
        #5
#            *    
#           ***   
#          *****  
#         ******* 
#         *********


def pattern8(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end='')
        for j in range(2*i-1):
            print("*",end='')
        for j in range(n-i):
            print(" ",end='')
        print()
        # 5
        # *********
        #  ******* 
        #   *****  
        #    ***   
        #     *    

def pattern9(n):
   for i in range(n):
       for j in range(n-i-1):
           print(" ",end='')
       for j in range(i+1):
           print("* ",end='')
       print()
   for i in range(n,0,-1):
       for j in range(n-i):
           print(" ",end='')
       for j in range(i):
           print("* ",end='')
       print()
    # 5
    #     * 
    #    * *    
    #   * * * 
    #  * * * * 
    # * * * * * 
    # * * * * * 
    #  * * * * 
    #   * * * 
    #    * * 
    #     * 

def pattern10(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end='')
        print()
    for i in range(n-2,0,-1):
        for j in range(i):
            print("* ",end='')
        print()

def pattern11(n):
    # start =1
    # for i in range(n):
    #     if i%2==0:
    #         start= 1
    #     else:
    #         start = 0
    #     for j in range(i+1) :
    #         print(" ",start)
    #         start = 1-start
    for i in range(1,n+1):
        for j in range(i):
            if (i+j)%2 ==0:
                print("0", end='')
            else:
                print("1", end='')
        print()

def pattern12(n):
    for i in range(1,n+1):
        # for j in range(1,i+1):
        #     print(j,end='')
        # for j in range(2*(n-1)):
        #     print("-",end='')
        for j in range(1,i+1):
            print(j,end=' ')
        for j in range(2*(n-i)):
            print(" ",end=' ')
        for j in range(i,0,-1):
            print(j,end=' ')
        print()

def pattern13(n):
    num=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(num,end=' ')
            num=num+1
        print()


def pattern14(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end='')
        print()


def pattern16(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(chr(65+i),end='')
        print()

def pattern17(n):
    # for i in range(n):
    #     #Space
    #     for j in range(n-i-1):
    #         print(" ",end='')
    #     #char    
    #     for j in range(i+1):
    #         print(chr(65+j),end='')
    #     #middle
    #     print(chr(65+i),end='')
    #     #reverse
    #     for j in range(i,-1,-1):
    #         print(chr(65+j),end ='')
    #     #Space
    #     for j in range(n-i-1):
    #         print(" ",end='')
    #     print()

    # for i in range(n):
    #     for j in range(n-i-1):
    #         print(" ",end='')
    #     ch= 'A'
    #     breakpoint = int((2*i+1)/2)
    #     for j in range(1,2*i+2):
    #         print(ch,end='')
    #         if j<=breakpoint:
    #             ch= chr(ord(ch+i))
    #         else:
    #             ch= chr(ord(ch-i))
    #     for j in range(n-i-1):
    #         print(" ",end='')
    #     print()
    for i in range(n):
        # Print spaces
        for j in range(n - i - 1):
            print(" ", end='')
        
        # Print characters in increasing order
        for j in range(i + 1):
            print(chr(65 + j), end='')
        
        # Print characters in decreasing order
        for j in range(i, 0, -1):
            print(chr(65 + j - 1), end='-')
        
        # Move to the next line
        print()


def pattern18(n):
    # for i in range(1,n+1):
    #     for j in range(i):
    #         print(chr(69-j),end='')
    #     print()
    letters= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(letters[n-j],end='')
        print()

def pattern19(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end='')
        for j in range(2*i):
            print(" ",end='')
        for j in range(n-i):
            print("*",end='')
        print()
    for i in range(n):
        for j in range(i+1):
            print("*",end='')
        for j in range(2*(n-i-1)):
            print(" ",end='')
        for j in range(i+1):
            print("*",end='')
        print()

def pattern20(n):
    # for i in range(n):
    #     for j in range(i+1):
    #         print("*",end='')
    #     for j in range(2*(n-i-1)):
    #         print(" ",end='')
    #     for j in range(i+1):
    #         print("*",end='')
    #     print()
    # for i in range(n):
    #     for j in range(n-i):
    #         print("*",end='')
    #     for j in range(2*i):
    #         print(" ",end='')
    #     for j in range(n-i):
    #         print("*",end='')
    #     print()
     # Upper half of the pattern
    for i in range(n):
        # Print left side asterisks
        for j in range(i + 1):
            print("*", end='')

        # Print spaces in between
        for j in range(2 * (n - i - 1)):
            print(" ", end='')

        # Print right side asterisks
        for j in range(i + 1):
            print("*", end='')

        # Move to the next line
        print()

    # Lower half of the pattern
    for i in range(n - 1):
        # Print left side asterisks
        for j in range(n - i - 1):
            print("*", end='')

        # Print spaces in between
        for j in range(2 * (i + 1)):
            print(" ", end='')

        # Print right side asterisks
        for j in range(n - i - 1):
            print("*", end='')

        # Move to the next line
        print()



def pattern21(N):
    for i in range(n):
        if(i==0 or  i== n-1):
            print("*"*(n))
        else:
            for j in range(n):
                if(j==0 or j==n-1):
                    print("*",end='')
                else:
                    print("",end='')
                print()

def pattern22(n):
    for i in range(2*n-1):
        for j in range(2*n -1):
            top=i
            bottom=j
            right=(2*n-2)-j
            left=(2*n-2)-i
            print(n-min(min(top,bottom),min(left,right)),end=' ')
        print()



n=int(input())
pattern22(n)