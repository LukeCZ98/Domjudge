S=str(input())
N=int(input())
elenco=[]
found=False
for i in range(N):
    elenco.append(str(input()))
for k in elenco:
    for j in elenco:
        if k!=j:
            if(k+j==S) or (j+k==S):
                found=True
elenco.sort()
elenco.reverse()
if found==True:
    print("OK",end="")
else:
    print(elenco[0]+elenco[N-1],end="")