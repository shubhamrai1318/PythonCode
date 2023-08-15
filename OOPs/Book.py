class Book:#Class
    def __init__(self,bookname,subject,price): #Constructor
        self.bookname=bookname
        self.price=price
        self.subject=subject
    def __str__(self):#ToSTring
        return "Name = {0}, Sub={1} Price={2}".format(self.bookname,self.subject,self.price)

b1=Book("Basic C","C",120)#Call the constructor
print(b1)#Call the toString
b2=Book("Basic C","C",120)#Call the constructor
print(b1,b2)
