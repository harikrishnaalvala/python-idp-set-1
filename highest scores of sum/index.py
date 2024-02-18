
n=int(input())
a=[]
for i in range(n):
    m=list(map(int,input().split(",")))
    a.append(m)
b=a[0]
for i in a:
    if sum(i)>sum(b):
        b=i
r=""
for i in b:
    r+=str(i)+" "
print(r)
