


n=int(input())
def fun(n):
    def fun2(k,k1,o,i):
        if(le>o):
            if(not(l[o]//k1==0)):
                l1.append(l[o]//k1)
                l1.append(100)
                l2=0
                while i<le and i<o:
                    l2+=l[i];
                    i+=1
                if(l2//k==0):
                    l1.append(k)

    def fun1(k,o,o2,i,le):
        if(le>o2):
            i=i
            l2=0
            while i<le and i<o:
                l2+=l[i];
                i+=1
            if(not(l2//k==0)):
                l1.append(l2//k)
                l1.append(k)
    if(n>999999999999 or n<-999999999999):
        return 'invalid'
    nege=0
    if(n<0):
        nege=1
        n=n*-1
    
    if n==0:
        return 'Zero'
    d={1:'One',2:'Two',3:"Three",4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:"Seventeen",18:'Eighteen',19:'Nineteen',20:'Twenty',30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred',1000:'Thousand',1000000:'Million',1000000000:'Billion'}

    s=0
    l=[]
    while n>0:
        l.append((n%10)*10**s)
        n=n//10
        s+=1
    print(l)
    le=len(l)
    print(le)
    l2=0
    l1=[]
    fun2(100000000,1000000000,11,6)
    fun1(1000000000,11,9,8,le)
    fun2(1000000,100000000,8,6)
    fun1(1000000,8,6,3,le)
    fun2(1000,100000,5,3)
    fun1(1000,5,3,3,le)

        # print(l2,l1)

    q1=[]
    if le>2:
        if(not(l[2]//100==0)):
            q1.append(l[2]//100)
            q1.append(100)
        q1.append(l[0]+l[1])
    elif le>1:
        q1.append(l[0]+l[1])
    elif le>0:
        q1.append(l[0])
    for i in q1:
        l1.append(i)
    print(l1)
    # print(q1)
    st=''
    for x in l1:
        if x in d:
            st+=d[x]+' '
        elif not(x==0):
            p=[]
            i=0
            while x>0:
                p.append((x%10)*10**i)
                x=x//10
                i+=1
            # print('pis ',p)
            p=p[::-1]
            if p[0] in d and p[1] in d:
                st+=d[p[0]]+'-'+d[p[1]]+' '
    if(nege==1):
        return 'Negative'+' '+st[:-1]
    return st[:-1]
print(fun(n))
# l=[100,101,110,111,1000,1001,1010,1011,1100,1101,1111,10000,10001,10010,10101,11111,200000,111000,111111,100000,999999,1234567]
# for i in range(1000000):
    # print(i,':',fun(i))
