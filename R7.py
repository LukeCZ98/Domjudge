def mcdr(A,B,R):
    if R==0:
        return B
    if R!=0:
        A=B
        B=R
        R=A%B
    return mcdr(A,B,R)

A=int(input())
B=int(input())
r=A%B
mcd=mcdr(A,B,r)
print(mcd,end="")