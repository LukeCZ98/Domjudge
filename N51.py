seq=[]
seq1=[]
count=0
elem=''
a=str(input())
while(a!='.'):
    seq.append(a)
    a=str(input())
b=str(input())
while(b!='.'):
    seq1.append(b)
    b=str(input())
for e in seq:
    for l in seq1:
        if e==l:
            count+=1
            elem+=e
if count>=1:
    print(elem[0],end="")
else:
    print("DISGIUNTE",end="")