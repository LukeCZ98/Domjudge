n=int(input())
n1=int(input())
sequenza=''
somma=0
cont=0
sequenza+=str(n)
sequenza+=str(n1)
while(n!=n1):
    n=n1
    n1=int(input())
    sequenza+=str(n1)
while(cont<len(sequenza)-1):
    if(sequenza[cont]!=0):
        somma+=int(sequenza[cont])
    if(sequenza[cont]=="0" and cont==0):
        print("0")
    if(sequenza[cont]=="0" and cont!=0):
        print(somma)
        somma=0
    cont+=1
