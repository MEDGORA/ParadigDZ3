board = [[" "," ", " "], [" "," ", " "], [" "," ", " "]]

win = False

def showBoard() :
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            print(board[i][j], end=' ')
        print()

def player1() :
    print("Первый игрок ставит крестик")
    print("Введите индекс ячейки [i][j] куда ставить Х")
    i = int((input("Bндекс i: ")))
    j = int(input("Bндекс j: "))
    if board[i][j] == " ":
        board[i][j] = "X"
    else :
        print("Данная ячейка уже занята, попробуйте снова")
        player1()

def player2() :
    print("Второй игрок ставит нолик")
    print("Введите индекс ячейки [i][j] куда ставить 0")
    i = int((input("Bндекс i: ")))
    j = int(input("Bндекс j: "))
    if board[i][j] == " ":
        board[i][j] = "0"
    else :
        print("Данная ячейка уже занята, попробуйте снова")
        player2()

def check() :
    global win
    for i in range(0, len(board)):
        if board[i][0] == board[i][1] == board[i][2] == "X" :
            print("Первый игрок победил!")
            win = True
        if board[i][0] == board[i][1] == board[i][2] == "0" :
            print("Второй игрок победил!")
            win = True

    if board[0][0] == board[1][1] == board[2][2] == "X" :
        print("Первый игрок победил!")
        win = True
    if board[0][0] == board[1][1] == board[2][2] == "0" :
        print("Второй игрок победил!")
        win = True

    if board[0][2] == board[1][1] == board[2][0] == "X" :
        print("Первый игрок победил!")
        win = True
    if board[0][2] == board[1][1] == board[2][0] == "0" :
        print("Второй игрок победил!")
        win = True


showBoard()
while win != True :
    player1()
    showBoard()
    check()
    if win == True :
        break
    player2()
    showBoard()
    check()
    if win == True :
        break