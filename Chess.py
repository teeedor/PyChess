# I want to Implement Chess in Python, playable from the command line
# will add gui use in later updates
# Need to Keep a Blog to pretend like im Teaching to Learn better

# The Board is a 2d array, X axis A-H (1-8), Y Axis 1-8
# pieces are defined as a tuple (color, piece, xloc, yloc)
# per color, 8 pawns, 2 rooks, 2 bishops, 2 horses, 1 king, 1 queen
# 32 total pieces

# functions
# create pieces - create a list with the starting chess pieces
def create_pieces():
    pieces = [('w', 'p', 1, 2), ('w', 'p', 2, 2), ('w', 'p', 3, 2), ('w', 'p', 4, 2),
              ('w', 'p', 5, 2), ('w', 'p', 6, 2), ('w', 'p', 7, 2), ('w', 'p', 8, 2),

              ('w', 'r', 1, 1), ('w', 'h', 2, 1), ('w', 'b', 3, 1), ('w', 'q', 4, 1),
              ('w', 'k', 5, 1), ('w', 'b', 6, 1), ('w', 'h', 7, 1), ('w', 'r', 8, 1),

              ('b', 'p', 1, 7), ('b', 'p', 2, 7), ('b', 'p', 3, 7), ('b', 'p', 4, 7),
              ('b', 'p', 5, 7), ('b', 'p', 6, 7), ('b', 'p', 7, 7), ('b', 'p', 8, 7),

              ('b', 'r', 1, 8), ('b', 'h', 2, 8), ('b', 'b', 3, 8), ('b', 'q', 4, 8),
              ('b', 'k', 5, 8), ('b', 'b', 6, 8), ('b', 'h', 7, 8), ('b', 'r', 8, 8)]
    return pieces


# Move - Check to see if it captures, check to see if there is a piece in the way
def move(pieces, x1, y1, x2, y2):
    # True - is capturing / False - Not Capturing
    capture = check_capture(pieces, x2, y2)
    # Check against the piece moveset
    move_check = check_move(pieces, x1, y1, x2, y2)
    # True - good path / False - bad path
    path = check_path(pieces, x1, y1, x2, y2)
    if capture and move_check and path:
        print("this")
        # make the move and change the board


# check_move - Checks that the move is within the moveset
def check_move(pieces, x1, y1, x2, y2):
    p1 = 0
    # find the starting piece
    for p in pieces:
        if (p[2] == x1) and (p[3] == y1):
            p1 = p
            print(p1)
    # Check to see if it is a valid move for the piece
    if p1[1] == 'p':
        inset = pawn_ms(p1[0], x1, y1, x2, y2)
    #
    # if p1[1] == 'r':
    #     inset = rook_ms(p1[0], x1, y1, x2, y2)
    # if p1[1] == 'h':
    #     inset = horse_ms(p1[0], x1, y1, x2, y2)
    # if p1[1] == 'b':
    #     inset = bishop_ms(p1[0], x1, y1, x2, y2)
    # if p1[1] == 'k':
    #     inset = king_ms(p1[0], x1, y1, x2, y2)
    # if p1[1] == 'q':
    #     inset = queen_ms(p1[0], x1, y1, x2, y2)


# check_capture - is the piece moving into another pieces space?
def check_capture(pieces, x1, y1, x2, y2):
    for p in pieces:
        if p[2] == x2 and p[3] == y2:
            return True
    return False


# MOVESETS
# Basic movements,  no capturing yet
def pawn_ms(color, x1, y1, x2, y2):
    if (color == 'w') and (y1 == 2) and (y1 == y2-2):
        return True
    if (color == 'w') and (y1 == (y2-1)):
        return True
    if (color == 'b') and (y1 == 7) and (y1 == y2+2):
        return True
    if (color == 'b') and (y1 == (y2+1)):
        return True
# def rook_ms
# def horse_ms
# def bishop_ms
# def king_ms
# def queen_ms


# check_path - Checks the path between movements
def check_path(pieces, x1, y1, x2, y2):
    print('this')


# Check_loc - Verifies that there is a piece at the given location
def check_loc(pieces, x, y):
    for p in pieces:
        if p[2] == x and p[3] == y:
            return True
    return False


# read_move - read the coords for piece to move from user
def read_move(pieces):
    while True:
        print('Which piece would you like to move?')
        x1 = input("X coord: ")
        y1 = input("Y coord: ")
        if check_loc(pieces, x1, y1):
            print('Which location would you like to move to?')
            x2 = input("X coord: ")
            y2 = input("Y coord: ")
            move = (x1, y1, x2, y2)
            return move
        else:
            print("There is no piece at that location. Please choose again. ")


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



