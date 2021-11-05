stringa=str(input())
sequenza=''
cont=0
strng=0
while(stringa!="."):
    stringa=str(input())
    if(stringa.isalpha()==False):
        cont+=1
    elif(stringa.isalpha()==True):
        strng+=1
    sequenza+=stringa
if(cont>0 and strng==0):
    print("NO",end="")
elif(strng>0 and cont>0):
    print("SI",end="")
elif(strng==0 and cont==0):
    print("NO",end="")