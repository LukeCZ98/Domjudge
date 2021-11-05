X=int(input())
A=[]
count=1
somma=0
for i in range(10):
    A.append([])
    for j in range(10):
        if count>X:
            count=1
        A[i].append(count)
        count+=1
for i in range(10):
    for j in range(10):
        if(i+j)==(10-1):
            somma+=A[i][j]
print(somma,end="")
