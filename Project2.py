import sys
from chessBoard import *

#CHESSBOARD= np.ndarray((8,8),dtype=object)


class Agent:
    def __init__(self, turn, colour):
        self.turn=turn #A flag that is true when its Computer's turn
        self.colour=colour
        self.attacked=0        
        self.attackedPieces=[]
        self.score=0

def game(user, chessBot):
    board=chessBoard()
    board.initializeBoard()
    board.displayChessBoard()

    while 1:
        print("\033[1;32;40m Enter current position and destined position\n")
        currentpos=input()
        destpos=input()
        board.moveChessPiece(currentpos,destpos, user)
        board.randomMoveChessPiece(chessBot)
        board.displayChessBoard()

user=Agent(True, "white")  #We will have two agents, user and chess bot
chessBot=Agent(False, "black")

game(user, chessBot)

#1. prompt user to enter his move (store moves as well)
#2. update chessboard
#3. Agent's turn (decide which move is the best using minmax and alpha puning)
#4. update chessboard
#5. display it
#6. repeat