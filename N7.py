N=int(input())
x=False
while(N!=5):
    if N%5==0:
        x=True
    N=int(input())
if x:
    print("ALMENO 1",end="")
else:
    print("NESSUNO",end="")