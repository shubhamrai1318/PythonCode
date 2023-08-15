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
        return "Roll_no={0}, Name={1},\t Phy={2}, Chem={3}, Math={4}".format(self.roll, self.name, self.phy, self.chem,
                                                                           self.math)


r1 = Result("1", "Rahul", 76, 45, 65)
r2 = Result("2", "Sachin", 23, 54, 32)
r3 = Result("3", "Mohit", 34, 55, 65)

results = [r1, r2, r3]
for r in results:
    print(r, "\t","\t","Total: ",r.total(),"\t",r.percent(),"%","\t",r.isPassed())

