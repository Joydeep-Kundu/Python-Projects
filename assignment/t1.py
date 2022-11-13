#1
#  basic_salary=int((input("Enter the Salary=")))
# dearness_allowance=0.40 * basic_salary
# rent=0.20 * basic_salary;
# print("Gross Salary=",(basic_salary-(dearness_allowance + rent)))

#2.1
#  km=int((input("Enter the distance in km=")))
# m = km*1000
# feet= km*3280.84
# inch=km*39370.1
# cm=km*100000
# print("IN M=",m)
# print("IN FEET=",feet)
# print("IN INCH=",inch)
# print("IN CM=",cm)

#2.2
# m1=int((input("Enter the marks of SUBJECT 1=")))
# m2=int((input("Enter the marks of SUBJECT 2=")))
# m3=int((input("Enter the marks of SUBJECT 3=")))
# m4=int((input("Enter the marks of SUBJECT 4=")))
# m5=int((input("Enter the marks of SUBJECT 5=")))
# total_marks=m1 + m2 + m3 + m4 +m5
# percentage=(total_marks / 500) * 100
# print("TOTAL MARKS=",total_marks)
# print("PERCENTAGE=",percentage)

#3
# length=int((input("Enter the length=")))
# breadth=int((input("Enter the breadth=")))
# radius=int((input("Enter the radius=")))
# print("AREA OF RECTANGLE=",length * breadth)
# print("PERIMETER OF RECTANGLE=",(2 * (length + breadth)))
# print("AREA OF CIRCLE=",3.14 * (radius ** 2))
# print("circumference OF CIRCLE=", 2 * 3.14 * radius)

#4
# C=int((input("Enter the value of C=")))
# D=int((input("Enter the value of D=")))
# print("ORIGINAL=",C,D)
# e=C
# C=D
# D=e
# print("INTERCHANGED=",C,D)

#5 
# a=int((input("Enter the 5digit value of =")))
# s=0
# d=0
# while(a>0):
#     d=a%10
#     s=s+d
#     a=a//10  
# print("Sum=",s)

#6
# a=int((input("Enter the 5digit value of =")))
# s=0
# d=0
# while(a>0):
#     d=a%10
#     s=s*10+d
#     a=a//10  
# print("Sum=",s)

#7
# a=int((input("Enter the 5digit value of =")))
# s=a%10
# d=0
# while(a>0):
#     d=a%10
#     a=a//10 
# print("Sum=",s+d)

#8
# lmp=35
# mp=52
# lp=48
# tp=80000
# ltp=tp*lp/100
# iltp=tp-tp*lp/100
# ilmp=((mp-lmp)*tp/100)
# ilwp=iltp-ilmp
# print("illiterate men=",ilmp)
# print("illiterate women=",ilwp)

#9
# amt=int((input("Enter the Amount value =")))
# print("100 rs notes=",amt//100)
# print("50 rs notes=",((amt%100)//50))
# print("10 rs notes=",((amt%100)%50)//10) 


#10
# s=float(input("enter selling price 15 items"))
# p=float(input("enter profit price 15 items"))
# print("cost price of one item is ",(s-p)/15)    

#11
# a=int(input())
# s=0
# while a>0:
#     d=(a%10)+1;
#     if(d>9):
#         d=d%10;
#     # print(s,d)
#     s=d+s*10;
#     a//=10
# n=s
# s=0
# while(n>0):
#    s=n%10+s*10;
#    n//=10 
# print(s)
  
n=int(input("enter you value"))
sum=0
m=n
while(n!=0):
   rem=n%10
   sum=sum+rem*rem*rem
   n=n//10
if(m==sum):
   print("amstrong")
else:
   print("not amstrong")