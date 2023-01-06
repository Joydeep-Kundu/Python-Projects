def new_func2(n):
    q=[]
    i=0
    while(n>0):
        q.append((n%10)*10**i)
        n=n//10
        i+=1
    return q;
def new_func1(l, i, d, st):
    if(l[i]/10**i in d):
        st=d[10**i]+' '+st
        st=d[l[i]/10**i]+' '+st
    return st
def new_func(l, d,st):
    
    if l[1]+l[0] in d:
        st=d[l[0]+l[1]]+st
    else:
        if l[0] in d:
            st=d[l[0]]+st
        if l[1] in d:
            st=d[l[1]]+'-'+st
    return st
n=int(input())

l=new_func2(n)
d={1:'one',2:'two',3:"three",4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:"seventeen",18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand',1000000:'milion'}
st=''
if(len(l)==1):
    print(d[l[0]])
elif(len(l)>1):
    st=new_func(l,d,st)
i=2
while(i<len(l)):
    if(len(l)>i+1):
        if l[i+1]>9000 and l[i+1]<100000:
            k=new_func2((l[i+1]+l[i])//1000)
            st=d[1000]+' '+st
            st=new_func(k,d,'')+' '+st
            i=i+1
        elif 10**i in d:
            st = new_func1(l, i, d, st)
    elif 10**i in d:
        st = new_func1(l, i, d, st)
    i+=1
print(st)
