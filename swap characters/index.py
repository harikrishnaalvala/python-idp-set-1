s=input()
t=input()
s1=list(s)
l1=list(t)
for i in range(len(s1)):
    if s1[i]!=l1[i]:
        temp=l1[i+1]
        l1[i+1]=l1[i]
        l1[i]=temp
        break
if s1==l1:
    print("Yes")
else:
    print("No")
        
