def cres(sec):
    subseq=[]
    for i in range(len(seq)-1):
        if(sec[i]<=sec[i+1]):
            subseq.append(sec[i])
        else:
            subseq.append(sec[i])
            subseq.append("-")
    return subseq

def maxlen(s):
    index=0
    for i in range(len(s)):
        if len(s[index])<len(s[i]):
            index=i
    return index

n=int(input())
seq=[]
if(n<0):
    print("Empty",end="")
else:
    seq.append(n)
    count=0
    lens=[]
    temp=''
    
    while(n>0):
        n=int(input())
        seq.append(n)
    sub=cres(seq)
    
    for el in sub:
        if el!="-":
            temp+=str(el)
        else:
            lens.append(temp)
            temp=''
    ind=maxlen(lens)
    print(lens[ind])
    print(len(lens[ind]),end="")