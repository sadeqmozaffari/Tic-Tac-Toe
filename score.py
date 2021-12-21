def who_win(array):
    if array[0][0] == 'X' and array[0][1] == 'X' and array[0][2] == 'X' or array[0][0] == 'X' and array[1][1] == 'X' and \
            array[2][2] == 'X' or \
            array[0][0] == 'X' and array[1][0] == 'X' and array[2][0] == 'X' or array[1][0] == 'X' and array[1][
        1] == 'X' and array[1][2] == 'X' or \
            array[2][0] == 'X' and array[2][1] == 'X' and array[2][2] == 'X' or array[0][2] == 'X' and array[1][
        2] == 'X' and array[2][2] == 'X' or \
            array[0][1] == 'X' and array[1][1] == 'X' and array[2][1] == 'X' or array[0][2] == 'X' and array[1][
        1] == 'X' and array[2][0] == 'X':
        print("Player1 X Win The Game")
        return True
    elif array[0][0] == 'O' and array[0][1] == 'O' and array[0][2] == 'O' or array[0][0] == 'O' and array[1][
        1] == 'O' and array[2][2] == 'O' or \
            array[0][0] == 'O' and array[1][0] == 'O' and array[2][0] == 'O' or array[1][0] == 'O' and array[1][
        1] == 'O' and array[1][2] == 'O' or \
            array[2][0] == 'O' and array[2][1] == 'O' and array[2][2] == 'O' or array[0][2] == 'O' and array[1][
        2] == 'O' and array[2][2] == 'O' or \
            array[0][1] == 'O' and array[1][1] == 'O' and array[2][1] == 'O' or array[0][2] == 'O' and array[1][
        1] == 'O' and array[2][0] == 'O':
        print("Player2 O Win The Game")
        return True
    else:
        count = 0
        for item in array:
            for contain in item:
                if contain == '-':
                    count += 1
                    if count != 0:
                        return False
                    else:
                        print("Draw")
                        return True
