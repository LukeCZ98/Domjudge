from math import log
n=int(input())
seq=[]
cont=0
if n==0:
    print("SI",end="")
else:
    seq.append(n)
    while(n!=0):
        n=int(input())
        seq.append(n)
    for i in range(len(seq)):
        num=str(bin(seq[i]))
        if(num.count('1')==1):
            cont+=1
    if(cont==(len(seq)-1)):
        print("SI",end="")
    else:
        print("NO",end="")

    
