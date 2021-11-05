def rvrs(lis,n,B):
    if n<0:
        return B
    if n>=0:
        B.append(lis[n])
    return rvrs(lis,n-1,B)

N=int(input())
A=[]
b=[]
for i in range(N):
    A.append(input())
c=rvrs(A,N-1,b)
for i in range(len(c)):
    print(c[i],end="")