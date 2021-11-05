frase=str(input())
alf='abcdefghijklmnopqrstuvwyxz'
al=list(alf)
for char in frase:
    if char!=" ":
        if char in al:
            al.remove(char)
if len(al)==0:
    print("SI",end="")
else:
    print("NO",end="")