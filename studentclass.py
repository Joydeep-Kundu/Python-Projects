class student:
    def getdata(self,a,b):
        self.name=a
        self.roll=b
    def showdata(self):
        print(self.name)
        print(self.roll)

class student1:
    def __init__(self,a,b):
        self.roll=b
        self.name=a
    def showdata(self):
        print(self.name,self.roll)

a1=student()
a1.getdata('sdf',12)
a1.showdata()
a2=student()
a2.getdata('sd',132)
a2.showdata()
s1=student1('abc',1)
s2=student1('ssd',2)
s1.showdata()
s2.showdata()
class crac:
    def live(self):
        print('have life')
class animal(crac):
    def bark(self):
        print('ohhhh')
class cat(animal):
    def like(self):
        print('like milk')
    def __del__(self):
        print('delete')
a1=cat()
a1.bark()
a1.like()
a1.live()
#desturcture is use to dealocate the memory space which is no more usefull to the program