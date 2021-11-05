mese=int(input())
if mese<1 or mese>12:
    print("MESE NON VALIDO",end="")
if mese==3:
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("INVERNO",end="")
    else :
        print ("PRIMAVERA",end="")
if mese==6 :
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("PRIMAVERA",end="")
    else :
        print ("ESTATE",end="")
if mese==9:
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("ESTATE",end="")
    else : print ("AUTUNNO",end="")
if mese==12 :
    giorno=int(input())
    if giorno>=1 and giorno<=20:
        print("AUTUNNO",end="")
    else :
        print ("INVERNO",end="")
if mese==1:
    print("INVERNO",end="")
if mese==2:
    print("INVERNO",end="")
if mese==4:
    print("PRIMAVERA",end="")
if mese==5:
    print("PRIMAVERA",end="")
if mese==7:
    print("ESTATE",end="")
if mese==8:
    print("ESTATE",end="")
if mese==10:
    print("AUTUNNO",end="")
if mese==11:
    print("AUTUNNO",end="")