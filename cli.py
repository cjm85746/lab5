# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board
from logic import get_winner
from logic import other_player

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player ='O'
    # count the turns, if the board are all filled up count>8, the game stops with draw.1
    count = 0

    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        for a in board:
            print (a)
        # TODO: Input a move from the player.
        print("input a row number (1-3)")
        a= int(input ())
        assert a>0 and a<4
        print("input a column number (1-3)")
        b=int (input())
        assert b>0 and b<4
        # TODO: Update the board.
        # if an user choose the slot that the other user already occupied, the game require the user to pick another slot.
        if board[a-1][b-1] != None:
            while board[a-1][b-1]!= None:
                print ("Choose an empty slot")
                print ("input a row number (1-3)")
                a= int (input())
                print ("input a column number (1-3")
                b=int (input ())
                assert b>0 and b<4
                assert a>0 and a<4
        board [a-1][b-1] = player
        count +=1

        #Check if there is an winner
        if get_winner(board) != None:
            print ("The winner is", player)
            winner =True
        # if the board is full and no winner the game is draw.
        if count ==9:
            print ("Draw")
            winner = True
        
        # TODO: Update who's turn it is.
        player = other_player(player)
        print ("Now it is", player, "'s turn")