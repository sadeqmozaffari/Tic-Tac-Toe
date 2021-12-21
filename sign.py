global not_add
global count
count = 2


def get_position(sign, array):
    row = int(input("which row ?: "))
    column = int(input("which column ?: "))
    if array[row - 1][column - 1] != '-':
        print("you can not add this position")
        return False
    else:
        array[row - 1][column - 1] = sign
        return True


def player_add_sign(array):
    global count
    if count % 2 == 0:
        player = 'Player1'
        sign = 'X'

    else:
        player = 'Player2'
        sign = 'O'

    count += 1

    print(f"please add the sign {player} ")
    get_pos = True
    while get_pos:
        assigned = get_position(sign=sign, array=array)
        if assigned:
            get_pos = False
