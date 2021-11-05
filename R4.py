def search(lis,n,num,occ,cont):
    if num==0:
        return cont
    elif(lis[n]==num):
        occ+=1
        cont+=1
        lis[n]="0"
    elif(n<0):
        n=len(lis)-1
        num=occ
        occ=0
    return search(lis,n-1,num,occ,cont)

X=int(input())
N=int(input())
A=[]
c=0
cont=0
for i in range(N):
    A.append(int(input()))
print(search(A,N-1,X,c,cont),end="")
