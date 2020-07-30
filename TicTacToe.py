print('\n' * 100)
print('Welcome to Tic-tac-toe')
def display_board(board):
    # Displays and clears Tic-tac-toe Board
    print()
    print('      |     | ')
    print('   ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('      |     | ')
    print('-----------------')
    print('      |     | ')
    print('   ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('      |     | ')
    print('-----------------')
    print('      |     | ')
    print('   ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('      |     | ')

def player_input():
    print()
    marker = ' '
    # Asks Players to assign X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Please pick a marker X or O: ')
    player1 = marker

    if player1 == 'X':
        player2='O'
    else:
        player2 = 'X'
    print(f'Thanks! Player 1 is now {player1} and Player 2 is {player2}.')
    return(player1, player2)



def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    #Check Rows, Columns, Diagonals
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))


import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    # Return True == Full Board
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position

def replay():
    choice = input('Play again? Enter Y or N ')

    return choice == 'Y' or 'y'

#Game code with all functions
while True:
    the_board = [' ']*10
    (player1_marker, player2_marker)= player_input()

    turn = choose_first()
    print()
    print(turn + ' will go first.')

    print()
    play_game = input('Creating the game board. Ready to play? Enter Y or N ')

    if play_game == 'Y' or 'y':
        game_on = True
    else:
        game_on = False
# Player 1
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 wins! Player 2 loses.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('No winner. It\'s a tie.')
                    game_on = False
                    break
                else:
                    turn = 'Player 2'
# Player 2
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 wins! Player 1 loses.')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('No winner. It\'s a tie.')
                    game_on = False
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
