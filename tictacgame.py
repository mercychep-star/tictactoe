# from IPython.display import clear_output
def display(board):
    print('\n' * 100)
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[7] + '|' + board[8] + '|' + board[9])


test_board = ['#', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']


# display(test_board)
# display(test_board)


def player_input():
    marker = ''
    while marker != 'X' and marker != 'Y':
        marker = input(" player 1, choose either X or Y:").upper()
        player1 = marker
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
        return player1, player2


# player1_marker, player2_marker = player_input()
# print(f"player 1 you take,{player1_marker} amd player 2 takes {player2_marker}")


def place_marker(board, marker, position):
    board[position] = marker


# place_marker(test_board,'%',8)
# display(test_board)
def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


# display(test_board)
#
#
import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'player 1'
    else:
        return 'player2'


def check_space(board, position):
    return board[position] == ''


def full_board_check(board):
    for i in range(1, 2):
        if check_space(board, i):
            return False
    return True


def player_choice(board, ):
    position = 0
    while position not in [1,2,3,4,5,6,7,8] or not check_space(board,position
    ):
        position = int(input('choose position: (1,9)'))
    return position
def replay():
   choice =  input("play again? enter YES or NO")
   return choice == 'YES'

