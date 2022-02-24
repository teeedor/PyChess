# coding=utf-8

# import functions written in Chess.py
from Chess import *
from Piece import *
from move_sets import *


def main():
    # MAIN LOGIC
    # before the game Starts
    board = create_pieces(3)
    turn = 'w'  # game starts with white

    while no_winner(board):  # While the game is running
        ma = read_move(board, turn)  # Read in the move from the Player (x1, y1, x2, y2)
        valid_move = move(board, turn, ma[0], ma[1], ma[2], ma[3])  # attempt to make the move

        if valid_move:
            turn = rotate_turn(turn)  # At the end of the turn, rotate it


main()