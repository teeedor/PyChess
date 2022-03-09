# I want to Implement Chess in Python, playable from the command line
# will add gui use in later updates
# Need to Keep a Blog to pretend like im Teaching to Learn better

# The Board is a 2d array, X axis A-H (1-8), Y Axis 1-8
# pieces are defined as a tuple (color, piece, xloc, yloc)
# per color, 8 pawns, 2 rooks, 2 bishops, 2 horses, 1 king, 1 queen
# 32 total pieces

# functions
# create pieces - create a list with the starting chess pieces
# NEED TO REWRITE WITH NEW PIECE OBJECT

from Piece import *
from move_sets import *


# modify this to make different boards for testing
def create_pieces(choice):
    if choice == 1:
        # full board reset
        pieces = [('w', 'p', 1, 2), ('w', 'p', 2, 2), ('w', 'p', 3, 2), ('w', 'p', 4, 2),
                  ('w', 'p', 5, 2), ('w', 'p', 6, 2), ('w', 'p', 7, 2), ('w', 'p', 8, 2),
                  ('w', 'r', 1, 1), ('w', 'h', 2, 1), ('w', 'b', 3, 1), ('w', 'q', 4, 1),
                  ('w', 'k', 5, 1), ('w', 'b', 6, 1), ('w', 'h', 7, 1), ('w', 'r', 8, 1),
                  ('b', 'p', 1, 7), ('b', 'p', 2, 7), ('b', 'p', 3, 7), ('b', 'p', 4, 7),
                  ('b', 'p', 5, 7), ('b', 'p', 6, 7), ('b', 'p', 7, 7), ('b', 'p', 8, 7),
                  ('b', 'r', 1, 8), ('b', 'h', 2, 8), ('b', 'b', 3, 8), ('b', 'q', 4, 8),
                  ('b', 'k', 5, 8), ('b', 'b', 6, 8), ('b', 'h', 7, 8), ('b', 'r', 8, 8)]

    if choice == 2:
        # two piece board
        pieces = [('w', 'k', 4, 4), ('b', 'k', 5, 5)]

    if choice == 3:
        # 4 piece board
        pieces = [('w', 'h', 1, 1), ('b', 'b', 5, 6), ('w', 'k', 8, 8), ('b', 'k', 7, 7)]

    return pieces


# read_move - read the coords for piece to move  - Return a tuple of the move
def read_move(pieces, turn):
    while True:
        if turn == 'w':
            color = 'White'
        else:
            color = 'Black'
        print('---------------------------------------')
        # print(pieces)
        print("It is {}'s turn".format(color))
        print('Which piece would you like to move?')
        x1 = input("X coord: ")
        y1 = input("Y coord: ")
        # in python 3, input returns a string not an int
        x1 = int(x1)
        y1 = int(y1)
        if check_color(pieces, turn, x1, y1):  # check for the right color and existence
            p = get_piece(pieces, x1, y1)  # retrieve the piece
            display_piece(p)
            print('Which location would you like to move to?')
            x2 = input("X coord: ")
            y2 = input("Y coord: ")
            x2 = int(x2)
            y2 = int(y2)
            move_attempt = (x1, y1, x2, y2)
            return move_attempt


# Display the chosen piece in a pleasant way
def display_piece(p):
    # check for color
    if p[0] == 'w':
        color = 'White'
    else:
        color = 'Black'
    # check for piece
    if p[1] == 'p':
        p_type = 'Pawn'
    if p[1] == 'r':
        p_type = 'Rook'
    if p[1] == 'h':
        p_type = 'Knight'
    if p[1] == 'b':
        p_type = 'Bishop'
    if p[1] == 'k':
        p_type = 'King'
    if p[1] == 'q':
        p_type = 'Queen'

    print("Color: {} / Type: {} / X Pos: {} / Y Pos: {}".format(color, p_type, p[2], p[3]))
    return 0


# Check_loc - Verifies that there is a piece at the given location of the correct color
def check_color(pieces, turn, x, y):
    for p in pieces:
        if p[2] == x and p[3] == y:
            if turn == p[0]:
                return True
            else:
                print("Wrong players turn (check_color())")
                return False
    print("There is no piece at location ({}, {}). Please choose again. ".format(x, y))
    return False


# search for the piece at the input location and return that tuple return a tuple of n, n, 0, 0 on no
def get_piece(pieces, x, y):
    for p in pieces:
        if p[2] == x and p[3] == y:
            return p
    n = ('n', 'n', 0, 0)
    return n


# Move - Check to see if it captures, check to see if there is a piece in the way
def move(pieces, x1, y1, x2, y2):
    # True - spaces are within the board, False outside board - Tested
    on_board = valid_loc(x1, y1, x2, y2)
    if on_board:
        on_board_string = 'On the Board'
    else:
        on_board_string = 'Not on the Board'

    # True - is capturing / False - Not Capturing - Tested
    capture = check_capture(pieces, x1, y1, x2, y2)
    if capture:
        capture_string = 'Capturing'
    else:
        capture_string = 'Regular Move'

    # Check against the piece moveset - Needs the rest of the moveset to be written
    move_check = check_move(pieces, capture, x1, y1, x2, y2)
    if move_check:
        move_check_string = 'valid move'
    else:
        move_check_string = 'bad move'

    # True - good path / False - bad path
    path = check_path(pieces, x1, y1, x2, y2)
    check_path_string = 'Check_path Not implemented'
    print("{} / {} / {} / {}".format(on_board_string, capture_string, move_check_string, check_path_string))

    if on_board and capture and move_check and path:
        print("Moving Piece from ({},{}) to ({},{})".format(x1, y1, x2, y2))
        # make the move and change the board
        make_move(pieces, capture, x1, y1, x2, y2)
        return True


# valid_loc - Checks that the moves are on the board
def valid_loc(x1, y1, x2, y2):
    if (x1 < 8) and (x1 > 0):
        if (y1 < 8) and (y1 > 0):
            if (x2 < 8) and (x2 > 0):
                if (y2 < 8) and (y2 > 0):
                    return True
    return False


# Maybe move to Piece Class
# check_capture - is the piece moving into another pieces space of the other color?
def check_capture(pieces, x1, y1, x2, y2):
    # get both pieces and compare their values
    p1 = get_piece(pieces, x1, y1)
    p2 = get_piece(pieces, x2, y2)  # might be empty space
    if p2[0] == 'n':
        return False
    else:
        if p1[0] != p2[0]:
            return True
        else:  # same color
            return False


# Maybe move to Piece Class
# check_move - Checks that the move is within the moveset
def check_move(pieces, capture, x1, y1, x2, y2):
    p1 = get_piece(pieces, x1, y1)
    if p1[1] == 'p':
        inset = pawn_ms(p1[0], capture, x1, y1, x2, y2)  # Check to see if it is a valid move for the piece
        return inset
    # if p1[1] == 'r':
    #     inset = rook_ms(p1[0], x1, y1, x2, y2)
    #     return inset
    if p1[1] == 'h':
        inset = horse_ms(x1, y1, x2, y2)
        return inset
    # if p1[1] == 'b':
    #     inset = bishop_ms(p1[0], x1, y1, x2, y2)
    #     return inset
    if p1[1] == 'k':
        inset = king_ms(x1, y1, x2, y2)
        return inset
    # if p1[1] == 'q':
    #     inset = queen_ms(p1[0], x1, y1, x2, y2)
    #     return inset


# Maybe move to Piece Class
# check_path - Checks the path between movements
def check_path(pieces, x1, y1, x2, y2):
    return False


# make_move - move the pieces at the location in the data structure
def make_move(pieces, capture, x1, y1, x2, y2):
    # move the pieces
    # change the x and y
    if capture:
            remove_piece(pieces, x2, y2)
    return pieces


# remove_piece - remove the piece from the input list, return the changed list
def remove_piece(pieces, x, y):
    i = 0
    for p in pieces:
        if p[2] == x and p[3] == y:
            rp = pieces.pop(i)
        i = i + 1
    return pieces


def rotate_turn(turn):
    if turn == 'w':
        return 'b'
    else:
        return 'w'


# no_winner - Check that both kings are still alive
def no_winner(pieces):
    kings = 0
    for p in pieces:
        if p[1] == 'k':
            kings = kings+1
    if kings == 2:
        return True



