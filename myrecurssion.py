#recursive ex is factorial
#factorial(n)=n*factoril(n-1)
#2 fn fac(n) n fac(n-1)
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
#fibinocci num 
f0=0
f1=1
f2=f1+f0
#f(n)=f(n-1)+f(n-2)
