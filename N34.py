X=int(input())
seq=[]
pari=[]
disp=[]
cresc=False
dis=False
n=0
if X==0:
    print("SI",end="")
else:
    for i in range(X):
        n=int(input())
        seq.append(n)
    for i in range(X):
        if(i%2==0):
            pari.append(seq[i])
        if(i%2!=0):
            disp.append(seq[i])
    for i in range(len(pari)-1):
        if(pari[i]<pari[i+1]):
            cresc=True
        else:
            cresc=False
    for i in range(len(disp)):
        if(disp[i]%2!=0):
            dis=True 
        else:
            dis=False
    if(cresc==True):
        if(dis==True):
            print("SI",end="")
        else:
            print("NO",end="")
    else:
        print("NO",end="")
