X=float(input())     #inserisco saldo mese iniziale
CanM=float(input())  #inserisco canone mensile
inter=float(input()) #inserisco la percentuale d'interesse
Y=(X-CanM)           #detraggo il canone a partire dal secondo mese
Y=round(Y+((inter*Y)/100)) #dal canone residuo,calcolo e aggiungo gli interessi
Z=(Y-CanM)           #idem qua,dal saldo attuale,detraggo il canone
Z=round(Z+((inter*Z)/100)) # e aggiungo gli interessi
print("PRIMO MESE:",round(X))  #
print("SECONDO MESE:",Y)       #stampo il tutto
print("TERZO MESE:",Z,end="")  #   