thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict),thisdict['year'])

# def r(str):
#     if len(str)==0:
#         return str;
#     return str[len(str)-1]+r(str[:len(str)-1])
# print(r('abcsd'))

# def f(num):
#     if num==0 or num==1:
#         return 1;
#     return num*f(num-1);
# print(f(5));
from asyncio.windows_events import NULL
from itertools import count
import math
from re import L
from stringprep import in_table_c5
import sys


def fib(num):
    if num==1 or num==2:
        return 1;
    return fib(num-1)+fib(num-2);
print(fib(12))

# n=int(input('enter range: '));
# i=0;
# a=1;
# b=1;
# count=1;
# while i<=n-1:
#     if i==0:
#         print(0,' ',end=(''));
#     elif i%2==0:
#         print(fib(a),' ',end=(''));
#         a+=1
#     elif i%2!=0:
#         print(2**b,' ',end=(''))
#         b+=1;
#     i+=1;
# num=input('enter 4 digit number ');
# num2=num[0]+num[2]+num[1]+num[3];
# num2=int(num2);
# print(num2);


# x=int(input('enter number '));
# l=[]
# num2=0;
# while x>0:
#     l.append(x%10);
#     x=int(x/10);
# i=3;
# while i>=0:
#     if(i==0 or i==3):
#         num2=num2*10+l[i];
#     elif(i==2):
#         num2=num2*10+l[i-1];
#     else:
#         num2=num2*10+l[i+1];
#     i-=1;
# print(num2);

# num=int(input('enter 4 digit number '));
# num=str(num);
# num2=num[0]+num[2]+num[1]+num[3];
# num2=int(num2);
# print(num2);
# print(l[::-1])

# c=3;
# x=int(input('enter number '));
# l=[]
# num2=0;
# while x>0: 
#     l.insert(0,x%10)
#     x=int(x/10);
#     c-=1;
# l[1],l[2]=l[2],l[1];
# i=0;
# while i<4:
#     num2=num2*10+l[i];
#     i+=1;
# print(num2);

# n=int(input('enter number '));
# c=1;
# e=0;
# o=0;
# while n>0:
#     if c%2==0:
#         e+=n%10;
#     else:
#         o+=n%10;
#     n=int(n/10);
#     c+=1;
# print(o-e,' even=',e,' odd=',o);

# --class--
# class student:
#     def __init__(self,r,n):
#         self.__roll=int(r);
#         self.__name=n;
#         self.dept='bca';
    
#     def display(self):
#         print(self.__roll,'  ',self.__name);

# s1=student(10,'abc');
# s1.display();
# print(s1.__name)

class stack:
    def __init__(self,s):
        self.__stk=[];
        self.__top=0;
        self.__size=s;
    def size(self):
        print(self.__size);
    def push(self,x):
        if self.__top==self.__size:
            print('Stack over flow');
            sys.exit();
        self.__stk[self.__top]=x;
        self.__top+=1;
        return 'success';
    def pop(self,x):
        if self.__top==0:
            print('stack under flow');
            sys.exit();
        y=self.__stk[self.__top];
        self.__stk[self.__top]=NULL;
        self.__top-=1;
        return y;
    def display(self):
        for i in range(self.__top+1):
            print(i);

# s1=stack(5);
# s1.push(2);
# s1.push(3);
# s1.display();

def func(m):
    i=1;
    while i<=3:
        a=math.floor(math.sqrt(m));
        if m==a*a:
            return True;
        m-=(a*a);
        i+=1;
    return False;
# i=1;
# while i<101:
#     if func(i)==True:
#         print(i);
#     i+=1;