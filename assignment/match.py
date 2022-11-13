import random
s=21
i=1
while s>0:
    if(s==1):
        break
    if(i%2!=0):
        while(1):
            try:
                p=int(input("enter no 1-4 "))
                if(p>0 and p<=4 and p<=s):
                    s=s-p
                    break
                print("invailid")
            except:
                print("invalid")
    else:

        if(s<=5):
            g=(s-1)
        else:
            g=random.choice([1,2,3,4])
        s-=g
        
        print("computer picked ",g)
    print("mathch stick= ",s)
    i+=1
if(s==0):
    if(i%2!=0):
        print("win")
    else:
        print("lose")
else:
    if(i%2==0):
        print("win")
    else:
        print("lose")
