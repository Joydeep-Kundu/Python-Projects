s=int(input())
e=int(input())
print()
for i in range(1,e):
    m=i*(i+1)
    if m>e:
        break
    if m>=s and m<=e:
        print(m)
print()
class account:
    def __init__(self,no):
        self.no=no
    def showno(self):
        print(self.no)
    def __add__(self,a):
        a=self.no+a.no
        return account(a)
    def __eq__(self,a):
        if self.no==a.no:
            return 1
        return 0
    def __ne__(self,a):
        if self.no!=a.no:
            return 1
        return 0
    def __le__(self,a):
        if self.no<=a.no:
            return 1
        return 0
    def __lt__(self,a):
        if self.no<a.no:
            return 1
        return 0
    def __ge__(self,a):
        if self.no>=a.no:
            return 1
        return 0
    def __gt__(self,a):
        if self.no>a.no:
            return 1
        return 0
    def __sub__(self,a):
        a=self.no-a.no
        return account(a)


a1=account(12)
a2=account(10)
a3=a1+a2
a3.showno()
print(a1<a2)
print(a1<=a2)
print(a1==a2)
print(a1!=a2)
print(a1>a2)
print(a1>=a2)
a4=a1-a2
a4.showno()
