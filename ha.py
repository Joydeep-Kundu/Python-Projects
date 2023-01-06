


# # n=int(input())
# def fun(n):
#     if(n>999999999999 or n<-999999999999):
#         return 'invalid'
#     nege=0
#     if(n<0):
#         nege=1
#         n=n*-1
    
#     if n==0:
#         return 'zero'
#     d={1:'one',2:'two',3:"three",4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:"seventeen",18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand',100000:'lakh'}

#     s=0
#     l=[]
#     while n>0:
#         l.append((n%10)*10**s)
#         n=n//10
#         s+=1
#     # print(l)
#     le=len(l)
#     # print(le)
#     l2=0
#     l1=[]



#     if(le>5):
#         i=3
#         l2=0
#         while i<le and i<6:
#             l2+=l[i];
#             i+=1
#         if(not(l2//1000==0)):
#             l1+=l2//100000,100000
#     if(le>3):
#         i=3
#         l2=0
#         while i<le and i<5:
#             l2+=l[i];
#             i+=1
#         if(not(l2//1000==0)):
#             l1+=l2//1000,1000
#         # print(l2,l1)

#     q1=[]
#     if le>2:
#         if(not(l[2]//100==0)):
#             q1.append(l[2]//100)
#             q1.append(100)
#         q1.append(l[0]+l[1])
#     elif le>1:
#         q1.append(l[0]+l[1])
#     elif le>0:
#         q1.append(l[0])
#     for i in q1:
#         l1.append(i)
#     # print(l1)
#     # print(q1)
#     st=''
#     j=0
#     print(l1)
#     for x in l1:
#         if x in d:
#             st+=d[x]+' '
#         elif not(x==0):
#             p=[]
#             i=0
#             while x>0:
#                 p.append((x%10)*10**i)
#                 x=x//10
#                 i+=1
#             # print('pis ',p)
#             p=p[::-1]
#             if p[0] in d and p[1] in d and len(l1)>5 and j<1:
#                 st+=d[p[0]]+' '+d[p[1]]+' '
#             elif p[0] in d and p[1] in d:
#                 st+=d[p[0]]+'-'+d[p[1]]+' '
            
#             j+=1
#     if(nege==1):
#         return 'Negative'+' '+st[:-1]
#     return st[:-1]
# print(fun(134))
# print(fun(134343))
# print(fun(12344))
