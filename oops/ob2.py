class item:
    def __init__(self,n,p,q) -> None:
        self.name=n
        self.price=p
        self.quantity=q
    def incresestock(self,q):
        self.quantity+=q
        self.display()
    def purchase(self,q):
        if self.quantity-q>0:
            self.quantity-=q
        else:
            print('failed')
        self.display()
    def display(self):
        print(self.name)
        print(self.price)
        print(self.quantity)
ob2=item('ab',12,121)
ob2.display()
ob2.incresestock(12)
ob2.purchase(12)
ob2.purchase(1211)
