result = {}
while True:
    print("0-Exit\t1-Add Details\t2-Search\t3-Search All")
    option = int(input(""))
    if option == 0:
        break
    if option == 1:
        roll = int(input("Enter the Roll Number of the Student: "))
        phy = int(input("Enter the Physics Marks: "))
        chem = int(input("Enter the Chemistry Marks: "))
        math = int(input("Enter the Mathematics Marks: "))
        total = phy + chem + math
        per = (total*100)/300

        result[roll] = [phy,chem,math,"total=",total,"percentage=",per]

    if option == 2:
        roll = int(input("Enter Roll Number: "))
        currentresult = result.get(roll)
        if currentresult == None:
            print("Details Not Availabe ")
        else:
            print(currentresult)


    if option == 3:
            print(result)






