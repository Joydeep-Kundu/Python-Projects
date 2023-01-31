class member:
    def __init__(self,n,c):
        self.name=n
        self.cardno=c
    def showdata(self):
        print(self.name,self.cardno)
class student(member):
    def __init__(self,bl,r, n, c):
        self.booklimit=bl
        self.roll=r
        member.__init__(self,n, c)
    def display(self):
        print(self.booklimit)
        print(self.roll)
        member.showdata(self)
ob1=student(101,12,'ad',112)
ob1.display()
class c:
    def __init__(self,n4):
        self.n4=n4
class a:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
class b(a,c):
    def __init__(self, n1, n2,n4):
        a.__init__(self,n1, n2)
        c.__init__(self,n4)
        self.n3=0
    def add(self):
        self.n3=self.n1+self.n2+self.n4
        print(self.n3)        
p=b(1,2,3)
p.add()