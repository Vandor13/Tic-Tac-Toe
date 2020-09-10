# write your code here

def print_matrix(matrix):
    print("---------")
    print("|", matrix[0][0], matrix[0][1], matrix[0][2], "|")
    print("|", matrix[1][0], matrix[1][1], matrix[1][2], "|")
    print("|", matrix[2][0], matrix[2][1], matrix[2][2], "|")
    print("---------")


def count_tictactoe(matrix):
    # initialize counter
    o = 0
    x = 0
    space = 0

    x_rows = 0
    o_rows = 0

    # count symbols
    for row in matrix:
        for symbol in row:
            if symbol == "X":
                x += 1
            elif symbol == "O":
                o += 1
            else:
                space += 1

    # count winning rows and columns
    for i in range(3):
        if matrix[i][0] == "X" and matrix[i][1] == "X" and matrix[i][2] == "X":
            x_rows += 1
        if matrix[0][i] == "X" and matrix[1][i] == "X" and matrix[2][i] == "X":
            x_rows += 1
        if matrix[i][0] == "O" and matrix[i][1] == "O" and matrix[i][2] == "O":
            o_rows += 1
        if matrix[0][i] == "O" and matrix[1][i] == "O" and matrix[2][i] == "O":
            o_rows += 1

    # count winning diagonals
    if sm[0][0] == "X" and sm[1][1] == "X" and sm[2][2] == "X":
        x_rows += 1
    if sm[0][2] == "X" and sm[1][1] == "X" and sm[2][0] == "X":
        x_rows += 1
    if sm[0][0] == "O" and sm[1][1] == "O" and sm[2][2] == "O":
        o_rows += 1
    if sm[0][2] == "O" and sm[1][1] == "O" and sm[2][0] == "O":
        o_rows += 1

    return x, o, space, x_rows, o_rows


def analyze_game_state(matrix):
    x, o, space, x_rows, o_rows = count_tictactoe(matrix)
    if (x_rows > 0 and o_rows > 0) or (not -1 <= (x - o) <= 1):
        return "Impossible"
        # print("Impossible")
    elif o_rows > 0:
        # print("O wins")
        return "O wins"
    elif x_rows > 0:
        return "X wins"
        # print("X wins")
    elif space == 0:
        return "Draw"
        # print("Draw")
    else:
        return "not finished"
        # print("Game not finished")


def clean_move(move_input):
    move_cleaned = [0, 0]
    if move_input[0] == 3:
        move_cleaned[1] = 2
    elif move_input[0] == 2:
        move_cleaned[1] = 1
    elif move_input[0] == 1:
        move_cleaned[1] = 0
    if move_input[1] == 3:
        move_cleaned[0] = 0
    elif move_input[1] == 2:
        move_cleaned[0] = 1
    elif move_input[1] == 1:
        move_cleaned[0] = 2
    return move_cleaned  # bla


sm = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print_matrix(sm)

x_turn = True

while analyze_game_state(sm) == "not finished":
    move = []
    legal_move = False
    while not legal_move:
        move = input("Enter the coordinates: ").split()
        try:
            move_unclean = [int(x) for x in move]
            move = clean_move(move_unclean)
            # print(move)
            if sm[move[0]][move[1]] != " ":
                print("This cell is occupied! Choose another one!")
            elif not (1 <= move_unclean[0] <= 3 and 1 <= move_unclean[1] <= 3):
                print("Coordinates should be from 1 to 3!")
            else:
                legal_move = True
        except ValueError:
            print("You should enter numbers!")

    if x_turn:
        sm[move[0]][move[1]] = "X"
    else:
        sm[move[0]][move[1]] = "O"
    x_turn = not x_turn
    print_matrix(sm)

print(analyze_game_state(sm))

# symbols = input("Enter cells: ")
#
# sm = [[symbols[0], symbols[1], symbols[2]], [symbols[3], symbols[4], symbols[5]], [symbols[6], symbols[7], symbols[8]]]
#
# print_matrix(sm)
#
# no_of_o, no_of_x, no_of_space, no_of_x_rows, no_of_o_rows = count_tictactoe(sm)
#
# # analyze_game_state(no_of_x_rows, no_of_o_rows, no_of_x, no_of_o, no_of_space)
#
# move = []
# legal_move = False;
# while not legal_move:
#     move = input("Enter the coordinates: ").split()
#     try:
#         move_unclean = [int(x) for x in move]
#         move = clean_move(move_unclean)
#         # print(move)
#         if sm[move[0]][move[1]] != "_":
#             print("This cell is occupied! Choose another one!")
#         elif not (1 <= move_unclean[0] <= 3 and 1 <= move_unclean[1] <= 3):
#             print("Coordinates should be from 1 to 3!")
#         else:
#             legal_move = True
#     except ValueError:
#         print("You should enter numbers!")
#
#
# sm[move[0]][move[1]] = "X"
#
# print_matrix(sm)
