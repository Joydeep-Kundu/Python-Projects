d={
    'index':[0,1,2,3,4,5,6,7,8,9,10,11],
    'state':['r','r','r','r','r','r','f','f','f','f','r','f']
}
li=[]
di={}
for i in d.keys():
    li.append(i)
    di[i]=[]
print(li)
for i in range(1,12):

    if d[li[1]][i-1]=='r' and d[li[1]][i]=='f':
        n=0
        for j in li:
            print(j)
            di[j].append(d[j][i-1]);
            n+=1
print(di)
