player1=input("Enter Player 1 name: ")
player2=input("Enter player 2 name: ")
original=21
for i in range(1,10):
    if original!=0:
        print(player1,"turn")
        c=int(input())
        if c>0 and c<6:
            original=original-c
            if original==0:
                print(player1," winner ")
            print("remaining= ",original)
        else:
            print("Enter Valid Number")
        print(player2,"turn")
        c=int(input())
        if c>0 and c<6:
            original=original-c
            if original==0:
                print(player2," is Winner")
            print("remaining=" , original)
