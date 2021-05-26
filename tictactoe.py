
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

def computerMove(letter):
    pass


#playing section
while usercommand == 'y':
    pass