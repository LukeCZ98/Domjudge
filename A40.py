seq=[]
n=int(input())
extmedia=[]
media=0
somma=0
minimo=0
if(n==-50):
    print("VUOTA",end="")
else:
    while(n!=-50):
        seq.append(n)
        n=int(input())
    for i in range(0,len(seq)):
        somma+=seq[i]
    media=somma//(len(seq))
    for elem in seq:
        if(elem>=media):
            extmedia.append(elem)
    minimo=min(extmedia)
    #print(seq)
    print(minimo,end="")
