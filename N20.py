stringa=str(input())
sequenza=''
strng=0
while(stringa!="."):
    sequenza+=stringa
    strng+=1
    stringa=str(input())
if(sequenza.isalpha()==True and strng>=1):
    print("SI",end="")
elif(sequenza.isalpha()==False and strng>=1):
    print("NO",end="")
elif(strng==0):
    print("SI",end="")