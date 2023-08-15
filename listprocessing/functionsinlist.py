l=[1,2,3,4,5]
print(l)
l1=l
print(l1,l)
l1=l1 + [0]
print(l1,l)
print(l1.__contains__(5))
print(l1.__contains__(59))
print(l)
l.pop()
print(l)
l.remove(3)#Value is removed
print(l)
l.pop(0)#Position is removed
print(l)
l.append("Apple")
print(l)
l.insert(1,"Mango")
print(l)
l=[3,2,4,6,-1]
l.sort()
print(l)
l=["Ball","Cat","Apple"]
l.sort()
print(l)
l=[3,2,4,6,-1]
l.sort(reverse=True)
print(l)