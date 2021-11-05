X=int(input())
N=int(input())
cont=0
somma=''
while(cont<N):
    cont+=1
    num=int(input())
    if((num%2==0) and num<X):
        somma+=str(num)
if(somma!=""):
    print(somma,end="")

