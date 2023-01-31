class student:
    def getdata(self,a,b):
        self.__name=a#name mingling
        self.__roll=b
    def showdata(self):
        print(self.__name)
        print(self.__roll)

class student1:
    def __init__(self,a,b):
        self.roll=b
        self.name=a
    def showdata(self):
        print(self.name,self.roll)

a1=student()
a1.getdata('sdf',12)
print()
# print(a1.__roll)
# print(a1.__name)
print()
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
#encapsulation and data hiding
#private datamember which cannot access outside of the class. it access by inside of the class
#start with dubble under sccore and end with maximam single _
#polymorphysism
#oparator overloading is most useful and importent example of polymorphysism
#inharitence