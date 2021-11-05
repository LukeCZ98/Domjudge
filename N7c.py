voto=4
A=0
B=0
C=0
totale=0
while voto!=0:
    voto=int(input())
    if voto==1:
        A=A+1
        totale=totale+1
    elif voto==2:
        B=B+1
        totale=totale+1
    elif voto==3:
        C=C+1
        totale=totale+1
if totale!=0:
    percA=A/totale*100
    percB=B/totale*100
    percC=C/totale*100
    percA=round(percA,1)
    percB=round(percB,1)
    percC=round(percC,1)
    if percA>50 or percB>50 or percC>50:
        print("1", A, percA)
        print("2", B, percB)
        print("3", C, percC)
        if percA>percB and percA>percC:
            print("VINCE 1",end="")
        elif percB>percC and percB>percC:
            print("VINCE 2",end="")
        else:
            print("VINCE 3",end="")
    else:
        print("1", A, percA)
        print("2", B, percB)
        print("3", C, percC)
        print("BALLOTTAGGIO",end="")
else:
    print("BALLOTTAGGIO",end="")