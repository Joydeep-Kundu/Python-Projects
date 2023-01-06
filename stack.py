class Stack:
    def __init__(self,size):
        self.__size=size;
        self.__arr=[0 for i in range(self.__size)]
        self.__top=-1;
    
    def spush(self,val):
        if self.__top==self.__size:
            return 'Stack overflow'
        self.__arr[self.__top]=val
        self.__top+=1
        return 'sucessfull'
    def spop(self):
        if self.__top==self.__size:
            return 'Stack underflow'
        self.__top-=1
        return self.__arr[self.__top+1]
    def ptop(self):
        return self.__top
o=Stack(5)
o.spush(23)
o.spush(2)
o.spush(22)
o.spush(2)
o.spush(22)
o.spush(2)
o.spush(22)
print(o.ptop())
      