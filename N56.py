pavim=[[0 for i in range(20)] for j in range(20)]

def visualizzaPavimento(pavimento, dim):
    for i in range(dim):
        for j in range(dim):
            if pavimento[i][j]==1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def est(pos,pas,penna,dim):
    global pavim

    if penna==True:
        if pas+pos[1]>=dim-1:
            pos[1]=dim-1
        else:
            pos[1]=pos[1]+pas
    else:
        if pas+pos[1]>=dim-1:
            for j in range(pos[1]+1,dim):
                pavim[pos[0]][j]=1
            pos[1]=dim-1
        else:
            for j in range(pos[1]+1,pos[1]+pas+1):
                pavim[pos[0]][j]=1
            pos[1]=pos[1]+pas
    return pos

def ovest(pos,pas,penna,dim):
    global pavim

    if penna==True:
        if pos[1]-pas<=0:
            pos[1]=0
        else:
            pos[1]=pos[1]-pas
    else:
        if pos[1]-pas<=0:
            for j in range(pos[1]-1,-1,-1):
                pavim[pos[0]][j]=1
            pos[1]=0
        else:
            for j in range(pos[1]-1,pos[1]-pas,-1):
                pavim[pos[0]][j]=1
            pos[1]=pos[1]-pas
    return pos

def sud(pos,pas,penna,dim):
    global pavim
    
    if penna==True:
        if pas+pos[0]>=dim-1:
            pos[0]=dim-1
        else:
            pos[0]=pos[0]+pas
    else:
        if pas+pos[0]>=dim-1:
            for i in range(pos[0]+1,dim):
                pavim[i][pos[1]]=1
            pos[0]=dim-1
        else:
            for i in range(pos[0]+1,pos[0]+pas+1):
                pavim[i][pos[1]]=1
            pos[0]=pos[0]+pas
    return pos

def nord(pos,pas,penna,dim):
    global pavim
    
    if penna==True:
        if pos[0]-pas<=0:
            pos[0]=0
        else:
            pos[0]=pos[0]-pas
    else:
        if pos[0]-pas<=0:
            for i in range(pos[0]-1,-1,-1):
                pavim[i][pos[1]]=1
            pos[0]=0
        else:
            for i in range(pos[0]-1,pos[0]-pas,-1):
                pavim[i][pos[1]]=1
            pos[0]=pos[0]-pas
    return pos

pennasu=False
pos=[0,0]
npos=[0,0]
cmd=[]
passi=0
c=int(input())
cmd.append(c)
while(c!=9):
    c=int(input())
    cmd.append(c)

for comd in cmd:
    if comd==1:
        pennasu=True
    elif comd==2:
        pennasu=False
    elif comd==3:
        passi=int(input("passi?"))
        print()
        npos=est(pos,passi,pennasu,20)
    elif comd==4:
        passi=int(input("passi?"))
        print()
        npos=ovest(pos,passi,pennasu,20)
    elif comd==5:
        passi=int(input("passi?"))
        print()
        npos=sud(pos,passi,pennasu,20)
    elif comd==6:
        passi=int(input("passi?"))
        print()
        npos=nord(pos,passi,pennasu,20)
    elif comd==7:
        visualizzaPavimento(pavim,20)
    pos=npos
