n=int(input())
a=[]
for i in range(n):
    if i%2==0:
        a.append(1)
    else:
        a.append(0)
print(*a)
for i in range(1,n):
    m=[]
    for j in a:
        if j==1:
            m.append(0)
        else:
            m.append(1)
    a=m
    print(*m)
