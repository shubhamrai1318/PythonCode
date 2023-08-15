class BankAccount():
    def __init__(self, name, acnumber, balance):
        self.name = name
        self.acnumber = acnumber
        self.balance = balance

    def deposit(self):
        amount = int(input("Enter Amount: "))
        if amount > 0:
            self.balance += amount
        else:
            print("\t Enter Valid Amount")

    def withdraw(self):
        amount = int(input("How much you want to withdraw: "))
        if amount < self.balance:
            if amount > 0:
                self.balance -= amount
            else:
                print("\tNegative Value Not Acceptable")
        else:
            print("\tLow Balance")

    def __str__(self):
        return "Name = {0}\t\tAccount Number = {1}\t\tBalance = {2}".format(self.name, self.acnumber, self.balance)


bankaccounts = {}
newaccountno = 0
while True:
    print(
        "0-Exit\t\t1-New Account\t\t2-Deoosit\t\t3-Withdraw\t\t4-Check Balance\t\t5-Close Accounts\t\t6-Total Accounts")
    option = int(input("Option: "))
    if option == 0:
        break
    if option == 1:
        newaccountno += 1
        name = input("Name = ")
        balance = int(input("Balance = "))
        newaccount = BankAccount(name, newaccountno, balance)
        bankaccounts[newaccountno] = newaccount
    if option == 2:
        accno = int(input("Enter account no: "))
        bankaccount = bankaccounts.get(accno)
        if bankaccount == None:
            print("Account Not Available")
            continue
        bankaccount.deposit()
    if option == 3:
        accno = int(input("Enter account no: "))
        bankaccount = bankaccounts.get(accno)
        if bankaccount == None:
            print(" Account Not Availavle")
            continue
        bankaccount.withdraw()
    if option == 4:
        accno = int(input("Enter account no: "))
        bankaccount = bankaccounts.get(accno)
        if bankaccount == None:
            print(" Account Not Available")
            continue
        print(bankaccount)
    if option == 5:
        accno = int(input("Enter account no to Close: "))
        bankaccount = bankaccounts.get(accno)
        if bankaccount == None:
            print(" Account Not Available")
            continue
        del bankaccounts[accno]

    if option == 6:
        print("Total Accounts ")
        for key in bankaccounts.keys():
            print("\t", bankaccounts[key])
