def max(a,b):
    if a>b:
        print(a)
    else:
        print(b)
def rMax(a,b):
    if a>b:
        return a #Return sends back a value and also ends the function
    return b
def maxMin(a,b):#Multiple return values
    if a>b:
        return a,b
    else:
        return b,a

result=max(2,3)
print(result)
result=rMax(2,1)
print(result*5)
result=maxMin(1,4)
print(result)
r1,r2=maxMin(73,5)
print(r1,r2)