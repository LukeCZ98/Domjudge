N=int(input())
cont=0
ver=0
ns=str(N)
while(cont<(len(ns))):
    if(ns[cont]=='0'):
        ver+=1
    cont+=1
    
if(ver>0):
    print("NO",end="")
elif(ver==0):
    print("SI",end="")

