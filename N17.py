num=int(input())
m=num
if(m!=0):
    
    num=int(input())
n=num
pari=False
multipli=False
while(num!=0):
    
    if(m%2==0 and n%2==0 and n!=0):
        pari=True
        

  
    if((m+n)%m==0 or (m+n)%n==0):
            multipli=True
            
            
    m=n        
    n=num=int(input())
    
if(pari or multipli):
    print("SI",end="")
else:
    print("NO",end="")