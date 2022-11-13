
import random
from copy import copy

sudo=[['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-']]
l=[9,2,3,4,5,6,7,8,1]
x=random.choice(l)
print(x)
i=0
q=copy(l)
while i<9:
    x=random.choice(q)
    sudo[0][i]=x
    q.remove(x)
    i+=1;
for i in sudo:
    print(i)
i=1
while i<3:
    j=0
    q=copy(l)
    while j<9:
        if j<3:
            qq=copy(q)
            for m in range(i):
                for n in range(3):
                    if sudo[m][n] in qq:
                        q.remove(sudo[m][n])
            x=random.choice(qq)
            sudo[i][j]=x
            q.remove(x)
        if j>=3 and j<6:
            qqq=copy(q)
            for m in range(i):
                for n in range(3,6):
                    print(m,n)
                    if sudo[m][n] in qqq:
                        q.remove(sudo[m][n])
            x=random.choice(qqq)
            sudo[i][j]=x
            q.remove(x)
        j+=1
    i+=1
for i in sudo:
    print(i)