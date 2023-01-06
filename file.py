# f=open('input1.txt','w')
# f.write(input())
# f.close()
# f=open('input1.txt')
# print(f.read())
# f.close()
# f=open('input2.txt','w')
# f.write(input())
# f.close()
# f=open('input2.txt')
# print(f.read())
# f.close()

# f=open('input3.txt','w')
# f.write('10 20 30 40')
# f.close()
# f=open('input3.txt')
# inp=[int(x) for x in f.readline().split()]
# print(inp)
# f.close()
# def sum(s):
#     if len(s)==0:
#         return 0
#     return s[0]+sum(s[1:])
# ot=sum(inp)
# f=open('output.txt','w')
# f.write(str(ot))
# f.close()
# f=open('output.txt')
# print(f.read())
# f.close()

def fetch(l,ind):
    s=l[ind]
    return s

try:
    f=open('input1.txt')
    str=f.readline()
    res=10/0
    lst=str.split()
    print(fetch(lst,2))
    f.close()
except IndexError:
    print('exception caught')
except FileNotFoundError:
    print('file not exist')
except ZeroDivisionError:
    print('ZeroDivisionError')
except:
    print('default exception handeler')
finally:
    # f.close()
    print('sf')
print('return the value at the specified index')

