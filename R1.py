def Fib(n):
    if n==0:
        return 2
    else:
        return 3*(n+1)*(Fib(n-1))

N=int(input())
print(Fib(N),end="")