bris=int(input())
s1=int(input())
c1=int(input())

if(c1==1):
    c1=11
elif(c1==3):
    c1=float(10.5)

s2=int(input())
c2=int(input())

if(c2==1):
    c2=11
elif(c2==3):
    c2=float(10.5)

if s1==s2:
    if c1>c2:
        print("VINCE GIOCATORE 1",end="")
    else:
        print("VINCE GIOCATORE 2",end="")
elif s2!=bris:
    print("VINCE GIOCATORE 1",end="")
else:
    print("VINCE GIOCATORE 2",end="")