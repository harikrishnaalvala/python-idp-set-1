a=input().split()
m=int(a[0])
n=int(a[1])
total=0
for i in range(1,m+1):
    b=list(map(int,input().split()))
    if i>1 and i<m:
        sum_of=b[0]+b[-1]
        total+=sum_of
    else:
        sum_of=sum(b)
        total+=sum_of
print(total)
