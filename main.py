# coding=utf-8

# import functions written in Chess.py
from Chess import *

def main():
    # MAIN LOGIC
    # before the game Starts
    start_board = create_pieces()
    board = start_board
    turn = 'w'  # game starts with white

    while no_winner(board):  # While the game is running
        move = read_move(board)  # read in the move user wants to make
        # move()
        turn = rotate_turn(turn)
