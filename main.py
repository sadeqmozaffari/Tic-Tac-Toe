from board import show_board
from score import who_win
from sign import player_add_sign

print("Welcome the to tic tac toe Game")
print("Player1:X   Player2:O")

row_1 = ['-', '-', '-']
row_2 = ['-', '-', '-']
row_3 = ['-', '-', '-']
array = [row_1, row_2, row_3]

show_board(array=array)

Continue = True
is_finished = False
while Continue:
    if not is_finished:
        player_add_sign(array=array)
        show_board(array=array)
        is_finished = who_win(array=array)
    else:
        print("Good Luck")
        Continue = False
