i=1;
while(i<5):
    j=1
    while(j<=i):
        if(j==1):
            print(i," ",end='');
        elif(j==2):
            print(i+3," ",end='');
        elif(j==3):
            print(i+5," ",end='');
        else:
            print(i+6," ",end='');
        j+=1
    i+=1
    print()

print()
print()
n=1
i=5
while i>0:
    j=1
    while j<5:
        if i<=j:
            print(n,' ',end='');
            n+=1
        else:
            print("   ",end='');
        j+=1
    i-=1
    print()

print()
i=1;
n=1
while(i<5):
    j=1
    while(j<=i):
        print(n,' ',end='')
        n+=1
        j+=1
    i+=1
    print()
i=1;
while(i<6):
    j=1
    while(j<=i):
        if(j%2!=0):
            print('1 ',end='')
        else:
            print('0 ',end='')
        j+=1
    i+=1
    print()
print()