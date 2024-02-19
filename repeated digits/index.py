n=input()
m=[]
for i in n:
    if n.count(i)>1 and i not in m:
        m.append(i)
print(len(m))
