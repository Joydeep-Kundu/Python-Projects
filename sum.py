l=input()
l=[int(i) for i in l.split()]
n=int(input())
i=0
while i<len(l)-1:
    j=i+1
    while j<len(l):
        if l[i]+l[j]==n:
            print(i,j)
        j+=1
    i+=1
