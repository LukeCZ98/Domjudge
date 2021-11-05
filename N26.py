s=str(input())
consec=0
sequenza=''
sequenza+=s
while(s!="*"):
    s=str(input())
    sequenza+=s
for i in range(len(sequenza)):
    if(sequenza[i].isupper()==True):
        if(sequenza[i+1].isupper()==True):
            consec+=1
    if(sequenza[i].islower()==True):
        if(sequenza[i+1].islower()==True):
            if(sequenza[i]==sequenza[i+1]):
                consec+=1
if(consec>0 and len(sequenza)>=2):
    print("SI",end="")
elif(consec==0 and len(sequenza)>=2):
    print("NO",end="")
elif(len(sequenza)<2):
    print("NO",end="")