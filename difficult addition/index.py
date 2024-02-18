n=input().split()
a=n[0]
b=n[1]
s=min(len(a),len(b))
count=0
for i in range(1,s+1):
    sum_of=int(a[-i])+int(b[-i])
    if sum_of>=10:
        count+=1
if count==0:
    print("Easy")
else:
    print("Hard")
