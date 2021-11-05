stringa=str(input())
sequenza=''
contnum=0
strng=0
while(stringa!="*"):
    if(stringa.isdigit()==True):
        contnum+=1
    sequenza+=stringa
    strng+=1
    stringa=str(input())
if(strng>0 and contnum>0):
    print("ALMENO UNA",end="")
elif(strng>0 and contnum==0):
    print("NESSUNA",end="")
elif(strng==0 and contnum==0):
    print("NESSUNA",end="")