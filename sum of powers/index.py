n=input().split()
sum_of=0
for i in n:
    if len(i)==1:
        pass
    else:
        p=int(i[-1])
        m=int(i[:-1])
        sum=m**p
        sum_of+=sum
print(sum_of)
