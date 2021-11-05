def Nmax(n):
    n=str(n)
    ns=str(n)
    ls=list(ns)
    mas=''
    while(len(ls)>0):
        mas+=str(max(ls))
        ls.remove(max(ls))
    mas=int(mas)
    return mas

def Nmin(n):
    n=str(n)
    ns=str(n)
    ls=list(ns)
    minn=''
    while(len(ls)>0):
        minn+=str(min(ls))
        ls.remove(min(ls))
    minn=int(minn)
    return minn


N=int(input())
res=Nmax(N)-Nmin(N)
print(res,end="")