seq=[]
cont=0

while cont!=100:
    x=int(input())
    seq.append(x)
    cont+=1

c=""
conta=0
d=[]
f=0
conta2=0
contad=0
visualizza=True
visualizza1=True


for elem in seq:
    if elem<-50 or elem>50:
        c+=str(elem)
        conta+=1
        
    if -50<=elem<=50:
        d.append(elem)
        f+=elem
        contad+=1
        conta2+=1

if contad>0:
    media=f/contad
    m=round(media,6)

if visualizza==True:
    if conta==0:
        print("VUOTO1")
    elif conta!=0:
        print(c,sep='')

if visualizza1==True:
    if conta2==0:
        print("VUOTO2",sep="",end="")
    elif conta2!=0:
        print(m,sep="",end="")