aereo=[0,0,0,0,0,0,0,0,0,0]
posti=0
disp=True
disp1=True
while(posti<10):
    area=int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    if(area==1):
        for i in range(0,5):
            if(aereo[i]==0):
                aereo.pop(i)
                aereo.insert(i,1)
                posti+=1
                disp=True
                print("Reparto fumatori, posto",i+1 )
                break
            else:
                disp=False

        if(disp==False):
            rep=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if(rep=="S"):
                for i in range(5,10):
                    if(aereo[i]==0):
                        aereo.pop(i)
                        aereo.insert(i,1)
                        posti+=1
                        disp1=True
                        print("Reparto NON fumatori, posto",i+1)
                        break
            if(rep=="N"):
                print("Il prossimo volo parte tra 3 ore")
    if(area==2):
        for i in range(5,10):
            if(aereo[i]==0):
                aereo.pop(i)
                aereo.insert(i,1)
                posti+=1
                disp1=True
                print("Reparto NON fumatori, posto", i+1)
                break
            else:
                disp1=False
        if(disp1==False):
            rep=input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if(rep=="S"):
                for i in range(0,5):
                    if(aereo[i]==0):
                        aereo.pop(i)
                        aereo.insert(i,1)
                        posti+=1
                        disp1=True
                        print("Reparto fumatori, posto",i+1 )
                        break
            if(rep=="N"):
                print("Il prossimo volo parte tra 3 ore")







