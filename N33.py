import random
from random import randint
random.seed(0)
user=0
pc=0
while(user<3) and (pc<3):
    s1=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    while(s1<1) or (s1>3):
        s1=int(input("Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):"))
    if s1==1:
        print("hai giocato sasso")
    if s1==2:
        print("hai giocato carta")
    if s1==3:
        print("hai giocato forbice")
    s2=randint(1,3)
    if s2==1:
        print("il PC ha giocato sasso")
    if s2==2:
        print("il PC ha giocato carta")
    if s2==3:
        print("il PC ha giocato forbice")
    if s1==s2:
        print("Pari:")
    elif s1==1 and s2==2:
        print("Vince il PC:")
        pc+=1
    elif s1==1 and s2==3:
        print("Vinci tu:")
        user+=1
    elif s1==2 and s2==1:
        print("Vinci tu:")
        user+=1
    elif s1==2 and s2==3:
        print("Vince il PC:")
        pc+=1
    elif s1==3 and s2==1:
        print("Vince il PC:")
        pc+=1
    elif s1==3 and s2==2:
        print("Vinci tu:")
        user+=1
    print(str(user)+"-"+str(pc))

if user>pc:
    print("Hai vinto la sfida!")
elif pc>user:
    print("Il PC ha vinto la sfida!")