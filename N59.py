n=int(input())
A=[]
sommacroce=0
sommaresto=0
for i in range(n):
    A.append([])
    for s in range(n):
        A[i].append(int(input()))
for e in range(n):
    for l in range(n):
        if(e==int(n/2)) or (l==int(n/2)):
            sommacroce+=A[e][l]
        else:
            sommaresto+=A[e][l]
if(sommacroce>sommaresto):
    print("OK",end="")
else:
    print("NO",end="")