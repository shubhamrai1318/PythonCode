class Currency:
    def __init__(self, rupee, paisa):
        self.total = rupee * 100 + paisa

    def __str__(self):
        rupee = self.total // 100
        paisa = self.total % 100
        return "₹ {0}.{1}".format(rupee, paisa)
    def __add__(self, other):
        #print(self,other)
        return Currency(0,self.total + other.total)
    def __gt__(self, other):
        if self.total>other.total:
            return True
        else:
            return False
    def __sub__(self, other):
        return Currency(0,self.total - other.total)
    def __mul__(self, other):
        return Currency(0,(self.total * other.total)//100)
    def __floordiv__(self, other):#//
        return Currency(0,self.total / other.total)
    def __truediv__(self, other):#/
        return Currency(0,self.total/other.total)
#1+2 + 3  1+2=3 + 3
c1 = Currency(1,5)
c2 = Currency(1,0)
print(c1*c2)
c3 = Currency(3,25)
print(c1,"\t",c2,"\t",c3)
sum = c1+c2+c3
print("Total =  \t\t",sum)
if c1>c2:
    if c1>c3:
        print("Greater =  \t\t",c1)
    else:
        print("Greater =  \t\t",c3)
else:
    if c2>c3:
        print("Greater =  \t\t",c2)
    else:
        print("Greater =  \t\t",c3)
diff=c1-c2
print("Difference = \t",diff)
mul = c1*c2
print("Multiplication =",mul)

