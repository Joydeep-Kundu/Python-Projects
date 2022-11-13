a=input()
b=input()
a=[int(i) for i in a.split()]
b=[int(i) for i in b.split()]
c=[]
i=0
j=0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
while j<len(b):
    c.append(b[j])
    j+=1

while i<len(a):
    c.append(a[i])
    i+=1

print(c)