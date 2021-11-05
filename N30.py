s=str(input())
seq=[]
cont=0
if(s=="*"):
    print("NO",end="")
else:
    seq.append(s)
    while(s!="*"):
        s=str(input())
        seq.append(s)
    for i in range(len(seq)-1):
        if(seq[i] == seq[i+1]):
            if(seq[i].isalpha() == True) and (seq[i+1].isalpha() == True):
                if(seq[i].isupper() == True) and (seq[i+1].isupper() == True):
                    cont+=1
                if(seq[i].islower() == True) and (seq[i+1].islower() == True):
                    cont+=1
    if(cont>0 and len(seq) >= 1):
        print("SI", end="")
    elif(cont==0 and len(seq) >= 1):
        print("NO", end="")