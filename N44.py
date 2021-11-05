A=[]
for i in range(26):
    A.append(str(input()))
N=int(input())
B=[]
for i in range(N):
    B.append(int(input()))
parola=''
for X in B:
    if X<26:
        parola+=A[X]
print(parola,end="")