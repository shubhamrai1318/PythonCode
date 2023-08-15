def setVakues():
    value=1
    for i in range(9):
        for j in range(9):
            board[i][j]=value
            value+=1
def printBoard(board):
    for i in range(9):
        for j in range(9):

            if j==3 or j==6:
                print("\t",end="")
            print(board[i][j],'\t', end="")
        print()
def createBoard():
    row = [i for i in range(9)]
    board = [row.copy() for i in range(10)]
    return  board

def boxToArray(board, rowno, colno):
    rowlimit = (rowno // 3 + 1) * 3
    collimit = (colno // 3 + 1) * 3
    a = []
    for i in range(rowlimit - 3, rowlimit):
        for j in range(collimit - 3, collimit):
            a.append(board[i][j])
    return a

board = createBoard()
setVakues()
printBoard(board)
l=boxToArray(board,3,3)
print(l)