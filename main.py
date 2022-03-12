# coding=utf-8

# import functions written in Chess.py
from Chess import *


def main():
    # MAIN LOGIC
    # before the game Starts
    visual = True
    board = create_pieces(1)
    turn = 'w'  # game starts with white
    while no_winner(board):  # While the game is running
        if visual:
            display_board(board)
        ma = read_move(board, turn)  # Read in the move from the Player (x1, y1, x2, y2)
        valid_move, board = move(board, ma[0], ma[1], ma[2], ma[3])  # attempt to make the move
        if valid_move:
            turn = rotate_turn(turn)  # At the end of the turn, rotate it
        else:
            print("not a valid move, try again!")


main()
