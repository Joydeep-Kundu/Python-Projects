import random
#1
# y=int(input("enter year"));
# if(y%400==0 or y%4==0):
#     print("leap year")


#assignment3
#1
# for i in range(10):
#     h=int(input())
#     if(h>40):
#         print("bounus",(h-40)*12)
#     else:
#         print("not do over time");
#2
# def fac(n):
#        if(n==1):
#              return 1
#        return n*fac(n-1)
# print(fac(5))
#3
#print(int(input("First="))**int(input("Second=")))
#5
# n=int(input("enter"))
# sum=0
# m=n
# while(n!=0):
#    rem=n%10
#    sum=sum+rem*rem*rem
#    n=n//10
# if(m==sum):
#    print("amstrong")
# else:
#    print("not")
#
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
        if s==10 :
            g=4
        elif s==9 or s==14 or s==18 or s==20 or s==17:
            g=3
        elif s==8 or s==13 or s==19 :
            g=2
        elif(s<=5):
            g=(s-1)
        else:
            g=(1)
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
#13
# a='123'
# for i in a:
#     for j in a:
#         for k in a:
#             if i!=j!=k:
#                 print(i,j,k)
        