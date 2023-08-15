def printAdd(a,b):
    print(a + b)
def returnAdd(a,b):
    print("add",a,b)
    return a+b

printAdd(7,8)

x=returnAdd(5,8)
x=1
y=2
z=3
result=returnAdd(x,y)
result=returnAdd(result,z)
print(result)

result=returnAdd(returnAdd(x,y),z)
print(result)