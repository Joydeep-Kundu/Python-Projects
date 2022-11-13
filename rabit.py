# def fib(num):
#     if num==1 or num==2:
#         return 1;
#     return fib(num-1)+fib(num-2);
# # print(fib(11)*2)

# i=0
# j=1
# s=2

m=1;
while(m<=12):
    i=1;
    j=0;
    k=2;
    s=0;
    while i<m:
        s=j+k
        j=k
        k=s
        i+=1
    print('ds:',j)
    print('child',k-j)
    m+=1