class Queue:
    def __init__(self,size):
        self.__size=size
        self.__arr=[0 for i in range(self.__size)]
        self.__top=0
        self.__buttom=-1
    def qpush(self,val):
        if self.__top==self.__size:
            return 'overflow'
        self.__arr[self.__top]=val
        self.__top+=1
        return 'Sucessfull'
    def pop(self):
        if self.__top==self.__buttom or self.__buttom==0:
            return 'underflow'
        self.__buttom+=1;
        return self.__arr[self.__buttom-1]
    def size(self):
        return self.__size
    def top(self):
        return self.__top
    def buttom(self):
        return self.__buttom

class Cirqueue:
    def __init__(self,size):
        self.__size=size;
        self.__arr=[0 for i in range(self.__size)]
        self.__top=0
        self.__buttom=-1
    def spush(self.val):
        if 

    
