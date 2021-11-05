bigl=int(input())
b=str(bigl)
primasomma=0
seconsomma=0
for i in range(0,int(len(b)/2)):
    primasomma+=int(b[i])
for c in range(int(len(b)/2),len(b)):
    seconsomma+=int(b[c])
if(primasomma==seconsomma):
    print("FORTUNATO",end="")
else:
    print("SFORTUNATO",end="")