board = [' ' for x in range(10)]

"""The game has 9 positions, board instantiates the positions with a list because lists are modifiable.
insertLetter function has two arguments (variables) that modifies the content in the list (board) by filling a letter into
a position
    """
def insertLetter(letter, pos):
    board[pos] = letter

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def spaceIsFree(pos):
    return board[pos] == " "

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or 
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True 
    while run:
        move = input("Please select a position between 1 to 9 to enter X: ")
        try:
            move = int(move)
            if move in range(10):
                if spaceIsFree(move):
                    run = False #this stops the loop. user plays only one turn at a time to allow the computer play its turn 
                    insertLetter("X", move)
                else:
                    print("this position has already been taken")
            else:
                print("Please type a number between 1 and 9")

        except:
            print("Please enter a number")

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0
    
    # this block of code only checks for winning moves to take or block the opponent each time the code runs 
    for let in ["O", "X"]:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let): #simulates placing 'O' or 'X' in an empty spot
                move = i
                return move # If placing 'O' or 'X' results in a win, computer should return that move
            
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main ():
    print ("""Welcome to the game
**********************
********************** """)
    printBoard(board)

    while not (isBoardFull(board)):
        if not (IsWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("You lose!")
            break
        
        if not (IsWinner(board, "X")):
            move = computerMove()
            if move == 0:
                print (" ")
            else:
                insertLetter("O", move)
                print('computer placed an O on position' , move , ':')
                printBoard(board)
        else:
            print ("You win!")
            break

        


    if isBoardFull(board):
        print ("Tie game")

name = input("Enter User name please: ")
print (f"Welcome to the game {name}")

# a = x = input("Do you want to play? (y/n)")
# if a.lower() == "y":
#     while True:
#         x = input("Do you want to play again? (y/n)")
#         if x.lower() == 'y':
#             board = [' ' for x in range(10)]
#             print('--------------------')
#             main()
#         else:
#             break

a = x = input("Do you want to play? (y/n)")
if a.lower() == "y":
    while True:
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
        while True:
            x = input("Do you want to play again? (y/n)")
            if x.lower() == 'y':
                board = [' ' for x in range(10)]
                print('--------------------')
                main()
            else:
                break
            break
        break