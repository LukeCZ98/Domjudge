N=int(input())
m=[]
prop=True
for i in range(N):
    m.append([])
    for j in range(N):
        m[i].append(int(input()))
temp=0
tmp=[]
r=0
c=0
while(r<N-1):
    for i in range(N-r):
        for j in range(c,N-2):
            if i==N-r or j==c:
                temp+=m[i][j]
    tmp.append(temp)
    temp=0
    r+=1
    c+=1 
print(tmp)