strn=""
vocale=0

while(strn!='*'):
    strn=str(input())
    if(strn=='a' or strn=='e' or strn=='i' or strn=='o' or strn=='u'):
        vocale+=1
if(vocale>=1):
    print("ALMENO 1 VOCALE",end="")
elif(vocale==0):
    print("NESSUNA VOCALE",end="")
    