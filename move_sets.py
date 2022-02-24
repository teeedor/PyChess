# MOVESETS
# Basic movements,  no capturing yet
def pawn_ms(color, capture, x1, y1, x2, y2):
    valid = False

    # White Movement
    if (color == 'w') and (y1 == 2) and (y1 == y2-2):  # special first movement
        valid = True
    if (color == 'w') and (y1 == (y2-1)) and (x1 == x2):  # regular movement
        valid = True
    # Capturing Case
    if (color == 'w') and capture and (y1 == (y2-1)) and (x2 == x1-1 or x2 == x1+1):
        valid = True

    # Black Movement
    if (color == 'b') and (y1 == 7) and (y1 == y2+2):  # special first movement
        valid = True
    if (color == 'b') and (y1 == (y2+1)) and (x1 == x2):  # regular movement
        valid = True
    # Capturing Case
    if (color == 'b') and capture and (y1 == (y2+1)) and (x2 == x1-1 or x2 == x1+1):
        valid = True
    return valid


# def rook_ms
def horse_ms(x1, y1, x2, y2):
    valid = False
    if abs(x1 - x2) == 1:
        if abs(y1 - y2) == 2:
            valid = True
    if abs(x1 - x2) == 2:
        if abs(y1 - y2) == 1:
            valid = True
    return valid
# def bishop_ms


def king_ms(x1, y1, x2, y2):
    valid = False
    if (x2 == x1-1 or x2 == x1+1 or x2 == x1) and (y2 == y1-1 or y2 == y1+1 or y2 == y1):
        valid = True
    return valid

# def queen_ms