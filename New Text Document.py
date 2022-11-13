#a=10;100000
#b=20;
#c=a+b;
#print(c)
#a='SIT'
#b='BCA'
#c=a+' '+b
#print(c);
#a=input("enter input")
#print(a)
#b=input('enter input');
#print(b)
#c=a+b;
#print(c);
# a=10
# print(id(a));
# print(type(a));
# a=20;
# print(id(a));
# d=True;
# print(type(d));
# str='Hello Bca'
# print(str);z
# str=str+" "+"0992"
# print(str[2:5])
# print(str[0:4])
# print(str[1:7])
# print(str*10)
#x= ["A","E","I","O","U"]
#y=["a","e","i","o","u"]
#print(x+y)
#print(x[:2])
#print(y[1:4])
#print(x[4:]+y[4:])
#a=10;
#print("da",a);
# inc=input('Enter');
# inc=int(inc)
# tax=0;
# l=100000;
# if inc>10*l:
#     tax=(l*5/100)+(2*l*10/100)+(5*l*15/100)+((inc-10*l)*30/100);
# print(tax);


#q1


# i=1;
# while i<11:
#     print(i);
#     i=i+1;

#q2

# i=10;
# while i>0:
#     print(i);
#     i=i-1;


#q3

# i=-10;
# while i<11:
#     if i>0:
#         print("+",i);
#     else:
#         print(i);
#     i=i+1;

#q4

# i=1;
# while i<=100:
#   print(i);
#   i+=2;

#q5

# i=1;
# while i<=100:
#     if i%3==0:
#         print(i)
#     i=i+1;

# q6

# i=100;
# while i>=10:
#     if i%5!=0:
#         print(i);
#     i=i-1;

# q7

# i=2;
# s=0;
# while i<=100:
#     s=s+i;
#     i=i+2;
# print(s);


#q8

# i=1;
# s=0;
# while i<=100:
#     s=s+i/i;
#     i=i+1;
# print(s);

#q9

# i=1;
# j=10;
# while i<=10:
#     print(i,'/',j);
#     i+=1;
#     j-=1;

#q10

# i=1;
# m=1;
# n=int(input("enter number= "));
# while i<=n:
#     m=m*i;
#     i=i+1;
# print(m);


#q11


# i=1;
# s=0;
# d=0;
# n=int(input('enter number= '));
# while i<=n:
#     print(i);
#     d=i;
#     i=s+i;
#     s=d;

# i=1;
# while i<=5:
#     j=1;
#     while j<=5:
#         if i>=j:
#             print(1,end='');
#         j+=1;
#     print();
#     i+=1;

# i=1;
# while i<=5:
#     j=1;
#     while j<=5:
#         if j>=i:
#             if j%2!=0:
#                 print(1,end='');
#             else:
#                 print(0,end='');
#         j+=1;
#     print();
#     i+=1;


# i=5;
# while i>=1:
#     j=5;
#     while j>=1:
#         if j<=i:
#             print(j,end='');
#         else:
#             print(" ",end='')
#         j-=1;
#     print();
#     i-=1;


# i=1;
# while i<=4:
#     j=4;
#     while j>=1:
#         if j<=i:
#             print(i,end=(''));
#         else:
#             print(' ',end=(''))
#         j-=1;
#     print();
#     i+=1;

# s=1;
# i=1;
# while i<=4:
#     j=1;
#     while j<=i:
#         print(s,end=(''));
#         j+=1;
#         s+=1;
#     print()
#     i+=1;

# p=0;
# s=1;
# i=1;
# while i<=4:
#     j=1;
#     while j<=i:
#         print(s,end=(''));
#         p=s;
#         j+=1;
#     print()
#     i+=1;

# s=1;
# i=1;
# while i<=5:
#     j=1;
#     while j<=i:
#         print(j*2,end=(''));
#         j+=1;
#     print()
#     i+=1;

# s=1;
# i=1;
# while i<=5:
#     j=1;
#     while j<=i:

# s=13;
# i=4;
# while i<=4:
#     j=4;
#     while j>=1:
#         if j<=i:
#             print(s,end=(''))
#             s-=2;
#         else:
#             print(' ',end=(''))
#         j-=1;
#     i+=1;
#     print();

i=1;
s=13;
while i<=4:
    j=4;
    k=2;
    while j>=1:
        if j<=i:
            if j==1:
                print(s-((i-1)*2),end=(''));
            else:
                print(s-((i-1)*2)-kx,end=(''));
        else:
            print(' ',end=(''))
        j-=1;
        k+=2;
    i+=1;
    print();