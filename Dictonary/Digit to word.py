digits = {}
while True:
    print("0-Exit\t1-Search\t2-All Elements of Dictionary")
    option = int(input(""))
    if option == 0:
        break
    if option == 1:
        number = int(input("Enter any number to get its word Value: "))
        word = digits.get(number)
        if word != None:
            print(word)
        else:
            word = input("Enter the word\t")
            digits[number]=word
    if option == 2:
        print(digits)
