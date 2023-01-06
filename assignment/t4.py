import string
import random
from itertools import permutations 
# def coun(s,c):
#     n=leng(c)
#     m=leng(s)
#     i=0
#     for j in range(c-1,s):
#         if c in s:
#             i+=1
#     return n
# print(coun('dsadd','da'))
# print('dadfsdaac'.count(''))
def join(s):
    if leng(s)==0:
        return ''
    return s[0]+join(s[1:])
def cout(s,c):
    k=0
    for i in s:
        if i==c:
            k+=1
    return k;
def leng(s):
    c=0
    for i in s:
       c+=1
    return c 
def lowe(s):
    if s=='':
        return ''
    o=ord(s[0])
    if o>=65 and o<=90:
        return chr(o+32)+lowe(s[1:])
    return chr(o)+lowe(s[1:])
def uppe(s):
    if s=='':
        return ''
    o=ord(s[0])
    if o>=97 and o<=122:
        return chr(o-32)+uppe(s[1:])
    return chr(o)+uppe(s[1:])
def splite(j,n):
    l=[]
    s=''
    for i in j:
        if i!=n:
            s+=i
        else:
            l.append(s)
            s=''
    if s!='':       
        l.append(s)
    return l


def inte(s):
    s=splite(s,' ');s=s[0]
    l=len(s)
    c=l-1
    i=0
    m=0
    while i<l:
        o=ord(s[i])-48
        if(o<1 or o>9):
            return 'Error';
        m+=o*10**c
        c-=1
        i+=1
    return m
#2
# print('0000011'.frombinarytoint)

#3
# s=input()
# i=int(input())
# s=s[:i]+s[i+1:]
# print(s)
#4
# i=input()
# l=0
# for x in i:
#     if x!=' ':
#         l+=1
# print(l)
#t5
# p=input()
# pl=p.split()
# for i in pl:
#     if len(i)%2==0:
#         print(i)
#t6
# s=input()
# l=leng(s)//2
# print(uppe(s[:l+1])+s[l+1:])

# a=input()
# b=a
# i=0
# while b!='':
#     i+=1
#     b=b[1:]
# d=0
# c=0
# j=0
# # print(i)
# while j<i-1:
#     if a[j]!=' ':
#         d+=1
#     else:
#         # print(d,c)
#         if d%2==0:
#             print(a[c:j])
#         c=j+1
#         d=0
#     j+=1
# # print(c)
# if (i-c)%2==0:
#     print(a[c:])

# l='12345'
# i=0
# while i<5:
#     if(i!=0):
#         l=l[:i*-1]+'*'*i
#     print('{}{}'.format(l,l[::-1]))
#     i+=1
# print()
# l='12345'
# l2='54321'
# i=0
# while i<5:
#     if(i!=0):
#         l=l[:i*-1]+'*'*i
#         l2=l2[:i-1]+'*'+l2[i:]
#     print('{}{}'.format(l,l2))
#     i+=1
# print()
# n=7
# for i in range(1,n):
#     for k in range(1,n-1):
#         if i+k<=n-1:
#             print(" ",end=' ')
#     for j in range(1,i+1):
#         print('*  ',end=' ')
#     print()
# i='i am good boys'
# while i!='':
#     d=0
#     try:
#         while i[d]!=' ':
#             d+=1
#     except:
#         d=d
#     if d%2==0:
#         print(i[:d])
#     i=i[d+1:]
# print()

# 7
# g=''
# i=input()
# for s in splite(i,' '):
#     g=g+uppe(s[0])+s[1:-1]+uppe(s[-1])+' '
# print(g)
#8
# s=input()
# c=0;ch=0
# for i in s:
#     o=ord(i)
#     if (o>=65 and o<=90) or (o>=97 and o<=122):
#         ch+=1
#     elif o>=48 and o<57:
#         c+=1
#     if(c>=1 and ch>=1):
#         print(True)
#         break
# if not(c>=1 and ch>=1):
#     print(False)

#9
# s=input()
# s=lowe(s)
# v='aeiou'
# print(s)
# c=0
# for i in v:
#     if i in s:
#         c+=1
# if c>=5:

#10
def coun(s,n):
    k=0
    j=0
    while j<leng(s):
        i=0
        print(s,k)
        nle=leng(n)
        while i<leng(s):
            if i+nle<=leng(s) and s[i:i+nle]==n:
                print('sfds')
                k+=1
                i+=nle-2
                break;
            i+=1
        j+=1
    return k
# print(coun('ssassasasasaa','sa'))
 #11
# s=input()
# i=0
# while i<len(s):
#    j=i+1
#    while j<len(s):
#        if s[i]==s[j]:
#            s=s[:j]+s[j+1]
#        else:
#            j+=1
#    i+=1
# print(s)

# 12
# s=input()
# d=dict()
# for i in s:
#     d[i]=d.get(i,0)+1
# j=list(d.keys())
# j=j[0]
# for i in list(d.keys())[1:]:
#     if d.get(j)>d.get(i):
#         j=i
# print(j)

#13
# s=input()
# d=dict()
# for i in s:
#     d[i]=d.get(i,0)+1
# j=list(d.keys())
# j=j[0]
# for i in list(d.keys())[1:]:
#     print(d.get(j),d.get(i))
#     if d.get(j)<d.get(i):
#         j=i
# print(j)

#14
# s=input()
# d={}
# for i in s:
#     d[i]=d.get(i,0)+1
# for i in d:
#     if d.get(i)%2!=0:
#         print(i,d.get(i))

#15
# s=[x for x in input().split()]
# d={}
# for j in s:
#     for i in j:
#         d[i]=d.get(i,0)+1
# print(d)

#16
# s=input()
# d={}
# for i in s:
#     if ord(i)>=48 and ord(i)<57:
#         d[i]=d.get(i,0)+1
# print(d)

#17
# s=input()
# jf=False;
# for i in s:
#     o=ord(i)
#     if not((o>=48 and o<=57) or (o>=65 and 0<=90) or (o>=97 and o<=122)):
#         print(True)
#         jf=True
#         break
# if not(jf):
#     print(False)

#18
s=input()
s=uppe(s)
le=len(s)
# print(random.choices(string.ascii_uppercase +string.digits, k=le))
ran=''.join(random.choices(string.ascii_uppercase +string.digits, k=le))
while ran!=s:
    ran=''.join(random.choices(string.ascii_uppercase +string.digits, k=le))
print(ran)

#19
# s=input()
# k=int(input())
# s=splite(s,' ')
# for i in s:
#     if leng(i)>k:
#         print(i)


#20
# s=input()
# ith=int(input())
# s=s[:ith]+s[ith+1:]
# print(s)

#21
# s=input()
# s=splite(s,' ')
# s=join(s)
# print(s)

#22
# s=input()
# m=input()
# s=splite(s,' ')
# for i in s:
#     if i[0]==m[0]:
#         print(i)
#23
# s1=input()
# s2=input()
# q=set(s1)
# p=set(s2)
# print(q-p,p-q)

#24
# s=input()
# i=0
# le=leng(s)
# while i<le:
#     if s[i]==',':
#         s=s[:i]+'.'+s[i+1:]
#     i+=1
# print(s)

#25
# permList = permutations(input())
# for perm in list(permList):
#     print (''.join(perm))

# 26
# d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
# i=lowe(input())
# print(d.get(i,'error'))

#27
# s=input()
# p=input()
# if p in s:
#     i=len(p)-1
#     j=0
#     le=len(s)
#     while j<le-i:
#         if s[j:j+i+1]==p:
#             print('word location',j,j+i+1)
#             break
#         j+=1
#28
# 29
# s=input()
# for i in range(len(s)):
#     print(s[i+1:]+s[:i+1])



# def climbStairs( n):
#     if(n<2):
#         return 1
#     return climbStairs(n-1)+climbStairs(n-2)
# for i in range(44):
#     print(climbStairs(i))
