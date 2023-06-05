def printnos(self,n):
    if n <1:
        return
    else:
        self.printnos(n-1)
        print(n)

n= int(input())
printnos(n)