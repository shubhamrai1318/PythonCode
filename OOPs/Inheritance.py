class Product():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return "name = {0}, price = {1}".format(self.name,self.price)

class Tax(Product):
    def __init__(self,name,price,tax):
        Product.__init__(self,name,price)
        self.taxv =price+tax
    def __str__(self):
        return "{0} \nWith Tax Price = {1}".format(Product.__str__(self),self.tax)

# p1=Product("Pepsi",40)
print("Available Brands\n pepsi and spirit")
name = input("select any one from above coldrinks: ")
if name == 'pepsi':
    t1=Tax(name ,40,4)
    print(t1)
elif name == 'spirit':
    t2=Tax(name,45,5)
    print(t2)