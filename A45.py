M=str(input())
m=''
count=M.count(" ")
if(M.startswith("_")):
    temp=list(M)
    temp.remove("_")
    for i in temp:
        if(i!="_"):
            m+=str(i)
    if m.isalnum()==True and count==0:
        print("SI",end="")
    else:
        print("NO",end="")
elif(M[0].isalpha()==True):
    tmp=list(M)
    for i in tmp:
        if(i!="_"):
            m+=str(i)
    if(m.isalnum()==True and count==0):
        print("SI",end="")
    else:
        print("NO",end="")
else:
    print("NO",end="")
