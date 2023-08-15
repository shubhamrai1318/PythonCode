#Create a list
l=[] # Blank list
print(l)
l=[1,2,3,4] #list with elements
print(l)
l=list()#Blank list
print(l)
l=list([1,2,3])#B list froma collection
print(l)
l=list(range(1,11))# list from a range
print(l)
#Adding alements to a list
l=[1]
print(l)
l= l + [2]
print(l)
l=[0] + l
print(l)
l=l + l
print(l)
#looping through a list
n=len(l)
print(n)
for i in range(n):
    print("l[{0}] = {1}".format(i, l[i]))
for item in l:
    print(item,type(item))
#Python list can elements of any type including list
l=["Apple",1,2.3]
print(l)
fruits=["Apple","Mango"]
l= l + [fruits]
print(l)
print(type(l))
print(type(l[0]))
print(type(l[3]))