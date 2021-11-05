m=int(input())
n=int(input())
valass=abs(m-n)
contnprimi=0
div1,count1=2,0
div2,count2=2,0
while div1<=m/2 and count1==0:
    if m%div1==0:
        count1+=1
    div1+=1
if count1==0:
    contnprimi+=1
while div2<=n/2 and count2==0:
    if n%div2==0:
        count2+=1
    div2+=1
if count2==0:
    contnprimi+=1

if(contnprimi<2):
    print("non entrambi primi",end="")
elif(contnprimi==2 and valass!=2):
    print("non gemelli",end="")
elif(contnprimi==2 and valass==2):
    print("gemelli",end="")

