N=70
ques=[]
for i in range(8):
    ques.append(int(input()))
stude=[]
for i in range(N):
    stude.append([])
    for j in range(9):
        stude[i].append(input())
mini=int(input())
voti=[]
supe=[]
cont=0
for i in range(N):
    voto=0
    for j in range(1,8):
        voto+=int(stude[i][j])*int(ques[j-1])
    voto+=int(stude[i][8])*int(ques[7])
    voti.append(voto)
for i in range(N):
    if voti[i]>=mini:
        print(stude[i][0], voti[i])
        cont+=1
        supe.append([stude[i][0],voti[i]])
minsup=[]
for i in range(len(supe)):
    minsup.append(supe[i][1])
ind=minsup.index(min(minsup))
mass=max(voti)
masstu=voti.index(mass)
print(cont, stude[masstu][0], supe[ind][0],end="")
