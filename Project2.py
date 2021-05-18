import sys
import numpy as np



class square:
    def __init__(self, identifier, state):
        self.identifier=identifier      #Each square has a unique identifier (h3,h4 etc)
        self.state=state    #Tells if a sqaure is empty or not

    

class chessBoard: #chessBoard will contain a 2D array of square instances

    def __init__(self):
        pass

    def initializeBoard():
        pass

    def placeChessPieces():
        pass

    def evaluationFunction():
        pass

    def displayChessBoard():
        pass
    
    def updateChessBoard():
        pass

class chessPiece:

    def __init__(self, name, colour, position):
        self.name=name
        self.colour=colour
        self.position=position


class Pawn(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'p',colour,position)

    def movementFunction():
        pass


class Bishop(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'b',colour,position)

    def movementFunction():
        pass


class Rook(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'r',colour,position)

    def movementFunction():
        pass


class Knight(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'k',colour,position)

    def movementFunction():
        pass


class Queen(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'Q',colour,position)

    def movementFunction():
        pass


   
class King(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'K',colour,position)

    def movementFunction():
        pass


class Agent:
    def __init__(self, turn):
        self.turn=turn #A flag that is true when its Computer's turn

