def printHello():#Signature of the function. Prints Hello 5 times
    print("Hello")#Body of the function
    print("Hello")
    print("Hello")
    print("Hello")
    print("Hello")

def printNHello(n): #n is a parameter. Parameter brings information into the function
    for i in range(n):
        print("Hello")

def printNMessage(n,message):
    for i in range(n):
        print(message)
def add():
    x=int(input("A="))
    y=int(input("B="))
    print(x+y)
def factorial(n=0):#DEfault value parameter
    print(n)


#printHello()#Calling the function


#printHello()
#printNHello(4)
#printNHello(7)
"""
add()
printNMessage(3,"Good Morning")
printNMessage(8,4)
x=int(input("N="))
printNHello(x)

printNMessage(message="Hi",n=3)#Named Parameters
printNMessage(3,"Bye")
"""
factorial(2)
factorial()
