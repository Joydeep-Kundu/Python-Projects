s='mca 1st sem'
l=[10,21,'items']
def fun():
    print('it is in function')

def fib(n,l=[0,1]):
    if n==1:
        return l[1]
    return fib(n-1,[l[1],l[0]+l[1]])


def tryb(n,l=[0,0,1]):
    if n==1:
        return l[2]
    return tryb(n-1,[l[1],l[2],l[1]+l[2]+l[0]])

if __name__=='__main__':

    print(fib(8))
    print(tryb(7))