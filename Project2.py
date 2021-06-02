import sys
from chessBoard import *


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
    playing=True

    while playing:
        print("\033[1;32;40m Enter current position and destined position\n")
        currentpos=input()
        destpos=input()
        board.minTurn = False
        
        if board.moveChessPiece(currentpos,destpos, user, board.array):                                      # PLAYER MOVE
            board.minTurn = True
            playing=board.checkWinning(user, chessBot)

            #board.randomMoveChessPiece(chessBot,user)
            #bestMove=Move(0,0,0,0)
            #bestMove=board.minmax(chessBot, user) 
            bestMove = board.findBestMoveAI(chessBot, user)
            board.noOfMovesHistory += 1

            print(bestMove.startY,bestMove.startX,bestMove.endY,bestMove.endX)
            startIdentifier = chr(ord('a') + bestMove.startY) + str(8 - bestMove.startX) 
            endIdentifier = chr(ord('a') + bestMove.endY) + str(8 - bestMove.endX) 
            
            board.moveChessPiece(startIdentifier,endIdentifier, chessBot, board.array)                       # BOT MOVE
            board.noOfMovesHistory += 1
            playing=board.checkWinning(user, chessBot)      # check winning after each move

            board.displayChessBoard()
            board.updateGamePhase()
        else:
            print("!!! Invalid Move !!!")
        board.checkPawnPromotion()

user=Agent(True, "white")  #We will have two agents, user and chess bot
chessBot=Agent(False, "black")

game(user, chessBot)

#1. prompt user to enter his move (store moves as well)
#2. update chessboard
#3. Agent's turn (decide which move is the best using minmax and alpha puning)
#4. update chessboard
#5. display it
#6. repeat