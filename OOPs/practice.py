import myfunctions as ro
class Result:
    def __init__(self, roll, name, phy, chem, math):
        self.roll = roll
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    def isPassed(self):
        if self.phy < 40 or self.chem < 40 or self.math < 40:
            return "\t\tFail"
        elif self.phy>60 or self.chem>60 or self.math>60:
            return "1st Division"
        else:
            return "2nd Division"
    def percent(self):
        per=(self.phy + self.chem + self.math)/3
        per=ro.roundOff(per)
        return per
    def total(self):
        tot=self.phy+self.chem+self.math
        return tot
    def __str__(self):
        return "Roll_no={0}, Name={1}, Phy={2}, Chem={3}, Math={4}".format(self.roll, self.name, self.phy, self.chem,
                                                                           self.math)
n=int(input("How many students details you want to add: "))
results=[]
for i in range(1,n+1):
    print("Enter Student ",i,"Details")
    rollno = int(input("Enter Roll_no:"))
    name = (input("Enter Name:"))
    phy = int(input("Physics Marks:"))
    chem = int(input("Chem Marks:"))
    math = int(input("Math Marks:"))
    r=Result(rollno,name,phy,chem,math)
    results =results +  [r]
for r in results:
    print(r, "\t","Total: ",r.total(),"\t",r.percent(),"%","\t",r.isPassed())

