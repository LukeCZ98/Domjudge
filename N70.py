S=str(input())
s=[]
s1=''
voc=["a","e","i","o","u"]
for i in range(len(S)):
    if S[i] in voc:
        s.append(S[i])
        s.append("f")
    s.append(S[i])
for l in range(len(s)//2,len(s)):
    s1+=s[l]
for c in range(0,len(s)//2):
    s1+=s[c]
print(s1,end="")
