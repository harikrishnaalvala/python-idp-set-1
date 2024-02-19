n=input().split()
a=int(n[0])
b=int(n[1])
m=list(map(int,input().split()))
c=[]
for i in range(b):
    x=int(input())
    c.append(x)
for j in c:
    count=0
    for d in m:
        if d>=j:
            count+=1
    print(count)
