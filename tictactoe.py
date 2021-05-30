import random

board=[' 'for x in range(10)]
print(board)
usercommand = input('Wanna Play ? y/n :')

def insertLetter(letter,pos):
    board[pos]=letter

def printboerd(board):
    print('  |    |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('  |    |   ')
    print('-----------')
    print('  |    |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('  |    |   ')
    print('-----------')
    print('  |    |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('  |    |   ')


def isBoardFull(board):
    return True if board.count(' ')>1 else False

def isWinner(board , letter):
    return ((board[1]==board[2]==board[3]==letter) or
    (board[4]==board[5]==board[6]==letter) or
    (board[7]==board[8]==board[9]==letter) or
    (board[1]==board[4]==board[7]==letter) or
    (board[2]==board[5]==board[8]==letter) or
    (board[3]==board[6]==board[9]==letter) or
    (board[1]==board[5]==board[9]==letter) or
    (board[3]==board[5]==board[7]==letter))


def userMove(board,letter):
    action = True
    while action:
        userInput=input('Please Enter the position : (between 1-9)')
        try:
            userInput=int(userInput)
            if userInput in range(1,10):
                if board[userInput] == ' ':
                    insertLetter(letter,userInput)
                    action = False
                else:
                    print('This Position is Occupid !')
            else:
                print('Your input is not between 1-9 !')
        except:
            print('Your input is not valid !')

def computerMove():
    #in this part we check the empty position of the board and saving their locations !
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    #just defining a move for computer position and it's initial position will be 0, an integer value not empty string ;)
    move=0 

    #for each letter of 'x' or 'o' we check that:
    for lett in ['O','X']:
        for i in possibleMoves:
            temp_board = board.copy()
            temp_board[i] = lett
            if isWinner(temp_board,lett):
                move = i
                return move
    
    #now we should check all the strategies , such as corner , middle and the edges
    #and priority of the strategies will consider as which is first 

    #First #corner
    freeCorner = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            freeCorner.append(i)

    if len(freeCorner) > 0 :
        move= random.choice(freeCorner)
        return move

    #second #middle
    if 5 in possibleMoves:
        move=5
        return move

    #Third #Edges
    freeEdges=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            freeCorner.append(i)

    if len(freeEdges) > 0:
        move=random.choice(freeEdges)
        return move




#playing section
while usercommand == 'y':
    pass