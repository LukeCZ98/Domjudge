n=0
errore=False
nstring=""
while(n!=-1):
    n=int(input())
    if(n>=0 and n<10):
        nstring=nstring+str(n)
    elif((n<0 or n>10) and n!=-1):
        errore=True

if(nstring=="" and n==-1):
    print("VUOTO",end="")
elif(errore==True):
    print("ERRORE",end="")
elif(errore==False and (int(nstring)%3==0)):
    print(nstring)
    print("SI",end="")
elif(errore==False and (int(nstring)%3!=0)):
    print(nstring)
    print("NO",end="")
