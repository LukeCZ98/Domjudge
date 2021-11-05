n=0
n1=0
count=0
cresc=True
decres=False
check=True
n1=int(input())
if(n1==0):
	print("NO",end="")
else:
	n=n1
	n1=int(input())
	if(n1<n):
		check=False
	count=2
	while(n1!=0):
		if(cresc==True and n1<n):
			cresc=False
			decres=True
		elif(cresc==False and n1>n) or (n1==n):
			check=False
		n=n1
		n1=int(input())
		count+=1
	if(check==True and count>3 and cresc==False and decres==True):
		print("SI",end="")
	else:
		print("NO",end="")
    