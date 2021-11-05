K=int(input())
A=[]
for i in range(K):
    A.append(int(input()))
N=int(input())
M=int(input())
B=[]
for i in range(N):
    B.append([])
    for j in range(M):
        B[i].append(0)
cont=0
p=0
r=N-1
s=0
c=M-1
ind=0

if N==M:
    if N!=1:
        B[N//2][M//2]=A[ind]
    else:
        B[N-1][M-1]=A[ind]
while(cont<(N*M)-1):
    for y in range(s,c):         #riga superiore
        if ind>K-1:              
            ind=0
        B[p][y]=A[ind]        
        ind+=1
        cont+=1
    for y in range(p,r):         #riga laterale destra
        if ind>K-1:              
            ind=0
        B[y][c]=A[ind]
        ind+=1
        cont+=1
    for y in range(c,s,-1):      #riga inferiore
        if ind>K-1:              
            ind=0
        B[r][y]=A[ind]
        ind+=1
        cont+=1
    for y in range(r,p,-1):       #riga laterale sinistra
        if ind>K-1:              
            ind=0
        B[y][s]=A[ind]         
        ind+=1
        cont+=1
    p+=1
    r-=1
    s+=1
    c-=1

for i in range(N):
    for j in range(M):
        print(B[i][j],end="")
    print()


        