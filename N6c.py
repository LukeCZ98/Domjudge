N=int(input())
if(N<=80):
    print("5",end="")
elif(N>80 and N<=140):
    importo=5+((N-80)*0.10)
    print(round(importo,3),end="")
elif(N>140 and N<=190):
    importo=5+(60*0.10)+((N-80-60)*0.07)
    print(round(importo,3),end="")
elif(N>190):
    importo=5+(60*0.10)+(50*0.07)+((N-80-60-50)*0.05)
    print(round(importo,3),end="")