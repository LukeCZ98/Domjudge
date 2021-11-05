N=90
matr=[]
risp=[]
stud=[]
punt=0
sol=str(input())
for i in range(N):
    matr.append(input())
    risp.append(input())
for i in range(N):
    temp=str(risp[i])
    for j in range(len(temp)):
        if(temp[j]==sol[j]):
            punt+=2
        elif(temp[j]=='X'):
            punt+=0
        elif(temp[j]!=sol[j]):
            punt-=1
    stud.append(punt)
    punt=0
for i in range(N):
    print(matr[i], stud[i])
