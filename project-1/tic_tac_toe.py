import random

def display_board(board):
    '''
    displays board in following format
    7 8 9
    4 5 6
    1 2 3
    numbers being the index of board list
    '''
    print('\n'*3) #extra spaces
    print(' '+'|'+' '+'|'+' ')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(' '+'|'+' '+'|'+' ')
    print('-----')
    print(' '+'|'+' '+'|'+' ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(' '+'|'+' '+'|'+' ')
    print('-----')
    print(' '+'|'+' '+'|'+' ')
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(' '+'|'+' '+'|'+' ')
    print('\n'*3) #extra spaces


def player_input():
    '''
    Accepts player input as X or O and validates it
    '''
    player1_choice = 'wrong'
    while player1_choice not in ['X', 'O']:
        player1_choice = input('Player 1 Please choose your symbol "X" or "O" : ')
        if player1_choice not in ['X', 'O']:
            print('Invalid input please try again')
    if player1_choice == 'X':
        player2_choice = 'O'
    else:
        player2_choice = 'X'

    return (player1_choice, player2_choice)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    '''
    Returns True if any winning combination is met
    '''
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #top row
    (board[4] == mark and board[5] == mark and board[6] == mark) or #middle row
    (board[1] == mark and board[2] == mark and board[3] == mark) or #bottom row
    (board[1] == mark and board[4] == mark and board[7] == mark) or #left column
    (board[2] == mark and board[5] == mark and board[8] == mark) or #middle column
    (board[3] == mark and board[6] == mark and board[9] == mark) or #right column
    (board[1] == mark and board[5] == mark and board[9] == mark) or #diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)) #diagonal


def choose_first():
    '''
    Randomly returns whther player 1 or 2 goes first
    '''
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    '''
    Returns True if space at position is empty on the board
    '''
    return board[position] == ' '


def full_board_check(board):
    '''
    Returns True if board is full
    '''
    for i in range(1,10):
        if space_check(board, i):
            return False

    return True        


def position_input(board, turn):
    '''
    asks for a player's next position (as a number 1-9) and then uses the function step_check to check 
    if its a free position. If it is, then return the position for later use
    '''
    position = 0 #for intial loop
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'{turn} Choose your next position (1-9) : '))
    return position


def replay():
    '''
    asks the player if they want to play again and 
    returns a boolean True if they do want to play again
    '''
    result = input('Do you want to play again? Enter Yes or No: ').lower()
    return result.startswith('y')


print('Welcome to Tic Tac Toe game')
while True: #keep loop running
    #Reset the board
    board = [' '] * 10 #initializing with spaces
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    game_on = True # flag for continuing game or not
    while game_on:
        #Player 1s turn
        if turn == 'Player 1':
            display_board(board)
            position = position_input(board, turn)
            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print('Congratulations Player 1 you have won the game')
                game_on = False
            
            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a draw')
                    break
            
                else:
                    turn = 'Player 2'
        
        #Player 2s turn
        else:
            display_board(board)
            position = position_input(board, turn)
            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations Player 1 you have won the game')
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print('Its a draw')
                    break
            
                else:
                    turn = 'Player 1'

    if not replay():
        break