voc=["a","e","i","o","u"]
count=0
chars=[]
vocal=''
temp=''
while(len(chars)<100):
    chars.append(str(input()))
for car in chars:
    if temp!=car:
        if(car in voc):
            count+=1
            temp=car
if(count<=1):
    print("OK",end="")
elif(count>1):
    print("ERRORE",end="")