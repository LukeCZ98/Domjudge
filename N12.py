N=int(input())
cont=1
ver=0

while(cont<=(N-1)/2):
    if(N%cont==0):
        ver+=1
    cont+=1


if(ver>1):
    print("NO",end="")
elif(ver==1):
    print("SI",end="")