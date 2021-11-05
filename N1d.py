X=500                #setto il saldo iniziale come dice la traccia
Y=round(int((X-5)+((2*X)/100)))  #detraggo il canone mensile di 5euro e aggiungo gli interessi sul canone appena calcolato
Z=round(int((Y-5)+((2*Y)/100)))  #idem qua,ricordandomi di arrotondare con la funzione round() le cifre del canone nei mesi
print("PRIMO MESE:",X,sep=" ")
print("SECONDO MESE:",Y,sep=" ")
print("TERZO MESE:",Z,sep=" ",end="")