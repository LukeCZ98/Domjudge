N=int(input())
X=0
C=0
sn=str(N)
sn+="*"
nN=[]
ss=''
for l in range(len(sn)-1):
    X+=1
    C=sn[l]
    if C!=sn[l+1]:
        nN.append(X)
        nN.append(int(C))
        X=0
for g in nN:
    ss+=str(g)

print(ss, len(ss),end="")