N=int(input())
cont=0
while(N!=0):
    N=int(input())
    if((N%2)!=0 and N%3==0):
        cont+=1
print(cont,end="")