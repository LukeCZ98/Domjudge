A=int(input())
B=int(input())
C=int(input())
if(A>=B+C or B>=A+C or C>=A+B):
    print("NO",end="")
elif(A==B and B==C):
    print("TRIANGOLO EQUILATERO",end="")
elif(A==B or B==C or A==C):
    print("TRIANGOLO ISOSCELE",end="")
else:
    print("TRIANGOLO SCALENO",end="")
