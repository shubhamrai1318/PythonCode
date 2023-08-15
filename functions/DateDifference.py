def cmpDate(d1,m1,y1,d2,m2,y2):
    # D1<D2 -ve, D1=D2 0, D1>D2 + ve
    if y1<y2:
        return -1
    if y1>y2:
        return 1
    if m1<m2:
        return -1
    if m1>m2:
        return 1
    if d1<d2:
        return -1
    if d1>d2:
        return 1
    return 0
def isleapyear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


def daysinmonth(month, year):

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if isleapyear(year):
            return 29
        else:
            return 28
    return 31


# Assume D1>D2
def daysDifference(d1,m1,y1,d2,m2,y2):
# D1>D2
    cmp=cmpDate(d1,m1,y1,d2,m2,y2)
    if cmp==0:
        return 0
    sign=1
    if cmp<0:
        sign=-1
        d1,d2=d2,d1
        m1,m2=m2,m1
        y1,y2=y2,y1
    diff1 = d1 - 1
    diff2 = d2 - 1
    diff3 = 0
    for i in range(1, m1):
        diff3 = diff3 + daysinmonth(i, y1)
    diff4 = 0
    for i in range(1, m2):
        diff4 = diff4 + daysinmonth(i, y2)
    sum = 0
    for year in range(y2, y1):
        if isleapyear(year):
            sum += 366
        else:
            sum += 365
    total = diff1 + diff3 - diff2 - diff4 + sum
    return sign*total
def isValidDate(d,m,y):
    return True
# print("Difference Between Date 1 and Date 2 is:\n\t", total, " Days")
d1 = 18#int(input("Enter Date 1: "))
m1 = 9#int(input("Enter Month 1: "))
y1 = 2020#int(input("Enter Year 1: "))
d2 = 18#int(input("Enter Date 2: "))
m2 = 9#int(input("Enter Date 2: "))
y2 = 2019#int(input("Enter Date 2: "))

result = daysDifference(d1,m1,y1,d2,m2,y2)
print(result)