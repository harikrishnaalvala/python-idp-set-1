n=input().split()
m=int(n[0])
a=int(n[1])

b=list(map(int,input().split()))
d=0
for i in range(1,a+1):
    if i%m==0:
        c=int(b[i-1])
        d+=(c)
print(d)
