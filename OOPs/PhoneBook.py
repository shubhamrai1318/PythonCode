class Person:
    def __init__(self, name, phonenumber):  # Self is a reference to the current object, The word self can be changed
        # print("Constructor called")#Constructor is alwas called __init__. It is called wneever an object is created
        self.name = name
        self.phonenumber = phonenumber

    def __str__(self):  # Gives a string representation of the object
        return "Name = {0}, Phone = {1}".format(self.name, self.phonenumber)
    def __gt__(self, other):
        if self.name>other.name:
            return True
        else:
            return False

p1 = Person("Sachin", "6576575")
p2 = Person("Rahul", "78767868")
print(p1 > p2)
"""
    print(p1.name)
    print(p1.phonenumber)
    print(p1)
    print(p2)
"""
phones = [p1, p2]
phones.sort()
print(phones)
for p in phones:
    print(p)
    d = {1: p1, 2: p2}
    print(d.get(2))
