# l=input()
l=64
print()
print()
d=-2
j=4*2
for i in range(1,j):
    if i<(j//2)+1:
        print((chr(l+i)+' ')*i)
    else:
        # print()
        s=((d+1)*-1)*'  '
        f=(chr(l+d+j//2+1)+' ')*(j-i)
        print(f'{s}{f}')
        d-=1