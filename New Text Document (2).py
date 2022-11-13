def fun():
    n=int(input())
    a=input()
    a=[int(i) for i in a.split()]
    b=input()
    b=[int(i) for i in b.split()]
    def Step(a, b, n):
        c = 0
        f = True
        

        while min(a)>-1:
            a = min(a)
            print('min',a)
            
            for i in range(n):
                if a[i]!= a:
                    print('arr',ar1[i],ar2[i])
                    a[i]-= b[i]
                    print(ar1)
                    c+= 1
                print(set(a))
            if len(set(a))==1:
                print(set(a))
                f = False
                print(c)
                break
        if f:
            print(-1)
    Step(a,b,n)
fun()
    