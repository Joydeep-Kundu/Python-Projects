# class vehical:
#     def __init__(self,r,m,md,c):
#         self.regno=r
#         self.make=m
#         self.model=md
#         self.color=c
# class comercial(vehical):
#     def __init__(self, r, m, md, c):
#         super().__init__(r, m, md, c)
#         self.loadcap=None
#     def display(self):
#         print(self.regno)
#         print(self.make)
#         print(self.model)
#         print(self.color)
#         print(self.loadcap)
#     def setloadcap(self,l):
#         self.loadcap=l
#     def getreg(self):
#         return self.regno
#     def getmodel(self):
#         return self.model
#     def getmake(self):
#         return self.make
#     def getcolor(self):
#         return self.color
#     def getloadcapacity(self):
#         return self.loadcap
    

# class passenger(vehical):
#     def __init__(self, r, m, md, c):
#         super().__init__(r, m, md, c)
#         self.passengercap=None
#     def display(self):
#         print(self.regno)
#         print(self.make)
#         print(self.model)
#         print(self.color)
#         print(self.passengercap)
#     def setpassengercap(self,p):
#         self.passengercap=p
#     def getmodel(self):
#         return self.model
#     def getreg(self):
#         return self.getreg
#     def getmake(self):
#         return self.make
#     def getcolor(self):
#         return self.color
#     def getpassengercapacity(self):
#         return self.passengercap

# class bus(passenger):
#     def __init__(self, r, m, md, c):
#         super().__init__(r, m, md, c)
#         self.noofdoor=0
#         self.doubledecker=None
#     def set(self,p,d,b:bool):
#         passenger.setpassengercap(self,p)
#         self.noofdoor=d
#         self.doubledecker=b
#     def display(self):
#         passenger.display(self)
#         print(self.noofdoor)
#         print(self.doubledecker)
#     def getnoofdoor(self):
#         return self.noofdoor
#     def getisdoubledecker(self):
#         return self.doubledecker
# b1=bus(1,'w',3,'red')
# b1.display()
# print()
# b1.set(50,3,2)
# b1.display()
# print()
# class car(passenger):
#     def __init__(self, r, m, md, c):
#         super().__init__(r, m, md, c)
#         self.noofdoor=0
#     def display(self):
#         passenger.display(self)
#         print(self.noofdoor)
#     def set(self,p,d):
#         passenger.setpassengercap(self,p)
#         self.noofdoor=d
#     def getnoofdoor(self):
#         return self.noofdoor
# c1=car(2,'va',2,'black')
# c1.display()
# print()
# c1.set(12,4)
# c1.display()
# print()
# class autorikshaw(passenger):
#     def __init__(self, r, m, md, c):
#         super().__init__(r, m, md, c)
#     def set(self,p):
#         passenger.setpassengercap(self,p)
# a1=autorikshaw(3,'anc',12,'white')
# print()
# a1.set(12)
# a1.display()

    