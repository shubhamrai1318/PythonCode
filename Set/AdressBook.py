name = 'Name'
p = 'Phone Number'
a = 'Adress'
l=[]
n=int(input("How Many Person Deatils You want to Add: "))
for i in range(n):
    d = {name: input("name: "),p: int(input("Phone_No: ")),a: input("Address: ")}
    l=l+[d]
    for i in l:
        print("Student : ",i)


