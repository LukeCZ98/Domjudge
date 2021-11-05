s=str(input())
seq=[]
voc=['a','e','i','o','u']
cons=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']
subseq=0
if(s!='.'):
    subseq+=1
while(s!='.'):
    seq.append(s)
    s=str(input())
for i in range(len(seq)-1):
    if(seq[i] in voc):
        if(seq[i+1] in voc):
            subseq+=1
    elif(seq[i] in cons):
        if(seq[i+1] in cons):
            subseq+=1
print(subseq,end="")

