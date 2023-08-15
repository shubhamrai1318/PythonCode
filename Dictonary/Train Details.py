 #Train DataBase

trains = {}
while True:
    print("0-Exit\t1-Add Train\t2-Search\t3-Search All\t4-Delete the Train")
    option = int(input("\n"))
    if option == 0:
        break
    if option == 1:
        train_no = int(input("Enter Train Number: "))
        train_name = trains.get(train_no)
        if train_name!=None:
            print("Already exists")
        else:
            train_name = input("Enter Train Name: ")
            trains[train_no] = train_name
            #n=int(input("press Y to add more train:"))
            #if n=='Y':



    if option == 2:
        train_no = int(input("Enter Train Number: "))
        train_name = trains.get(train_no)
        if train_name == None:
            print("Not Found\n Try Again")
        else:
            print(train_name)
    if option == 3:

        if not bool(trains):
            print("No Any Trains are Availabe To show")
        else:
            print(trains)

    if option == 4:
        train_no = int(input("Enter Train Number to Delete"))
        train_name = trains.get(train_no)
        if train_name != None:
            del trains[train_no]
        else:
            print("Train not available")


