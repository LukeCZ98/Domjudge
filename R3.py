def nonric(mat,n):
    somma=0
    for i in range(n):
        for j in range(n):
            if (i+j)==(n-1):
                somma+=mat[i][j]
    return somma

def ric(mat,N,i,j,som):
    if i==N:
        return som
    if (i+j)==N-1:
        som+=mat[i][j]
    return ric(mat,N,i+1,j-1,som)
n=int(input())
matr=[]
somma=0
for i in range(n):
    matr.append([])
    for j in range(n):
        matr[i].append(int(input()))
i=0
j=n-1
print(nonric(matr,n),end="")
print(";",end="")
print(ric(matr,n,i,j,somma),end="")