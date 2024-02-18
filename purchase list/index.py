n=list(map(int,input().split()))
a=None
for i in n:
    count=n.count(i)
    if count==1:
        a=i
        break
print(a)
a=None
for i in n:
    count=n.count(i)
    if count>=2:
        a=i
        break
print(a)
        
