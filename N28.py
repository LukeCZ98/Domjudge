s=str(input())
seq=[]
consec=0
if(s=="*"):
    print("NO",end="")
else:
    seq.append(s)
    while(s!="*"):
        s=str(input())
        seq.append(s)
    for i in range(len(seq)-1):
        if(seq[i]==seq[i+1]):
            consec+=1
    if(consec>0 and len(seq)>1):
        print("SI",end="")
    elif(consec==0 and len(seq)>1):
        print("NO",end="")
    elif(consec==0 and len(seq)==1):
        print("NO",end="")
