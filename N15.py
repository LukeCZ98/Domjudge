n=int(input())
n1=int(input())
cont=0
contsec=0
sequenza=[]
sequenza.append(n)
sequenza.append(n1)
if(n==n1 and n1==9):
    cont+=1
elif(n==n1 and n1!=9):
    cont=0
while(cont<2):
    n=n1
    n1=int(input())
    sequenza.append(n1)
    if(n==n1 and n1==9):
        cont+=1
    elif(n==n1 and n1!=9):
        cont=0
for i in range(len(sequenza)-3):
    if(sequenza[i]==sequenza[i+1]):
        if(sequenza[i]==sequenza[i+2]):
            contsec+=1
print(contsec,end="")
