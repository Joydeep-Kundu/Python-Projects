l=[6,9,2,5,3,10,-1,1,6,18];
max=l[0]
min=l[0]
i=1
print(len(l))
a=len(l)
while i<(a-1):
    if l[i]<l[i+1]:
        if l[i]<min:
            min=l[i];
        if l[i+1]>max:
            max=l[i+1]
    else:
        if l[i+1]<min:
            min=l[i+1];
        if l[i]>max:
            max=l[i]
    i+=2
if(a%2==0):
    if l[i]<min:
        min=l[i]
    if l[i]>max:
        max=l[i]

print(min,max)
