l=[3,1,12,21,123,1,12,6,66,32]
def margesort(l):
    le=len(l)
    if le==1:
        return l;
    l1=margesort(l[:le//2])
    l2=margesort(l[(le//2):])
    return merge(l1,l2)
def merge(a,b):
    c=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    while i<m:
        c.append(a[i])
        i+=1
    while j<n:
        c.append(b[j])
        j+=1
    return c
print(l)
print(margesort(l))
