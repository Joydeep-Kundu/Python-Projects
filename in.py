def fun(a,b):
    i=a-1
    c=0
    while(i>0):
        if(i==b):
            return c
        if(a%i==0):
            c+=1
            print(i)
            a=i
            i=i-1
        i-=1
    return c;
def fun2(N):

    x,y=[int(x) for x in N.split()]
    if(x==y):
        return 0
    c=fun(x,y)
    c+=fun(y,x)
    return c
N=input();
print(fun2(N))