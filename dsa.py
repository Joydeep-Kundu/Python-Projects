T=int(input())
i=0
while i<T:
    s=0
    s2=0
    a=input()
    g,p=[int(x) for x in a.split()]
    n=int(input())
    for y in range(n):
        o=input()
        ss,ss2=[int(x) for x in o.split()]
        print('sd',ss,ss2)
        s+=ss
        s2+=ss
    print(s*g+s2*p,s,s2,g,p)
    i+=1
