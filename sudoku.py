import random






sudo=[['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-']]
s=[]
l=[1,2,3,4,5,6,7,8,9];
x=random.choice(l)
for i in sudo:
    print(i)
print(x)
i=0
q=copy(l)
save=[]
dele=[]
while i<9:
    x=random.choice(q)
    q.remove(x)
    sudo[0][i]=x
    dele.append([x])
    if i>2:
        save.append(x)
    i+=1
print(save,dele)
for i in sudo:
    print(i)

##2
j=1
x=0
while(j<9):
    q=copy(l)
    i=0
    while i<9:
        qq=copy(q)

        for xx in dele[i]:
            if xx in qq:
                qq.remove(xx)
        try:
            x=random.choice(qq)
        except:
            i-=1
            break;
        sudo[j][i]=x
        dele[i].append(x)
        if x in q:
            q.remove(x)
        if x in save:
            save.remove(x)
        i+=1
    for i in sudo:
        print(i)
    j+=1
print(save,q)