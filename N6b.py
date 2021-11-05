ticket=float(input())
cond=int(input())
if(cond==0):
    print(round(ticket,3),end="")
elif(cond==1):
    importo=ticket-((ticket*10)/100)
    print(round(importo,3),end="")
elif(cond==2):
    importo=ticket-((ticket*15)/100)
    print(round(importo,3),end="")
elif(cond==3):
    importo=ticket-((ticket*25)/100)
    print(round(importo,3),end="")


