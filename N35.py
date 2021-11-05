seq=[]
summ=0
mis=str(input())
while(mis!="0"):
    seq.append(mis)
    mis=str(input())
for i in range(0,len(seq)-1,2):
    if(seq[i+1]=="s"):
        summ+=int(seq[i])
    elif(seq[i+1]=="m"):
        summ+=(int(seq[i]))*60
    elif(seq[i+1]=="h"):
        summ+=(int(seq[i]))*60*60
print(summ,end="")