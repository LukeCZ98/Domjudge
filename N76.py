M=int(input())
N=int(input())
fest=[]
giud=[]
cant=[]
for i in range(M):
    fest.append([])
    for j in range(N):
        fest[i].append(int(input()))
cont=0
for i in range(M):
    for j in range(N):
        if fest[i][j]>5:
            cont+=1
    giud.append(cont)
    cont=0
cont=0

for j in range(N):
    for i in range(M):
        cont+=fest[i][j]
    cant.append(cont)
    cont=0
b=0
for l in range(1,M):
    if giud[b]<=giud[l]:
        b=l
s=0
for p in range(1,N):
    if cant[s]>=cant[p]:
        s=p

print(b, s,end="")
