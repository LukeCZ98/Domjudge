N=int(input())
consec=0
x=int(input())
while(x!=-1):
    if(x<=N):
        consec+=1
    if(x>N and consec<N):
        consec=0
    x=int(input())
if(consec>=N):
    print("OK",end="")
elif(consec<N):
    print("NO",end="")