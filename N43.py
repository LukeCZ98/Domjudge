s=str(input())
count=0
p1=True
p2=True
if(s[0]==")") or (s[len(s)-1]=="("):
    p1=False
for char in s:
    if char=="(":
        count+=1
    elif char==")":
        count-=1
        if count<0:
            p1=False
            break
for i in range(len(s)-1):
    if(s[i]=="(") and (s[i+1]==")"):
        p2=False
        break
if(count==0 and p1==True):
    print("ok1")
else:
    print("no1")
if(p2==True):
    print("ok2")
else:
    print("no2")
