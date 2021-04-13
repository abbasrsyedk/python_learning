#factorial recursive

def calac_factorial(n):
    if(n==1):
        return 1 
    else:
        return n*(calac_factorial(n-1))


print(calac_factorial(5))