def check(lis,n,c,f):
    if(c==n/2):
        if(f==N):
            return True
    if(lis[c]!=lis[f]):
        return False
    return check(lis,n,c+1,f+1)

N=int(input())
if(N%2!=0):
    print("NO",end="")
else:
    A=[]
    cont=0
    s=N//2
    for i in range(N):
        A.append(int(input()))

    if check(A,N,cont,s)==True:
        print("SI",end="")
    else:
        print("NO",end="")