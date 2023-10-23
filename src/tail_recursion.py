def factorial(n, p=1):
    if n<=1:
        return p
    else:
        return factorial(n-1,n*p)
    
res = factorial(6)
print("factorial =",res)


        