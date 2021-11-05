N=int(input())
rmb=[]
cont=0
tmp=1
rmb.append(tmp)
while(cont<N-1):
    tmp+=2
    rmb.append(tmp)
    cont+=1
tmp2=0
while(cont>0):
    tmp2=rmb[cont]-2
    rmb.append(tmp2)
    cont-=1
somma=0
for l in rmb:
    somma+=l
print(somma,end="")