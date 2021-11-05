n=[]
count=0
while(len(n)<10):
    n.append(int(input()))
X=int(input())
for cifra in n:
    if(cifra%X==0):
        count+=1
if(count==0):
    print("OK",end="")
elif(count>0):
    print("NO",end="")