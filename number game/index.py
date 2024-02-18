n=list(map(int,input().split(",")))
m=int(input())
f=n[m:]
s=n[:-m]
r=""
for i in f:
    r+=str(i)+" "
print(r)
a=""
for i in s:
    a+=str(i)+" "
print(a)

    
