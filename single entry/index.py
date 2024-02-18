n=list(map(int,input().split()))
for i in n:
    count=n.count(i)
    if count==1:
        print(i)
    
