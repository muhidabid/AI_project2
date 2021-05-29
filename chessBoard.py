import numpy as np
import copy
import random

import tables
from chessPieces import *
from generateMoves import *

class square:
    def __init__(self, identifier, isEmpty):
        #self.boxColour="\033[1;30;47m"
        self.textStyle="1"      # bold by default
        self.textColour="33"    # yellow by default
        self.boxColour="46m"    # white by default
        

        self.identifier=identifier                      # Each square has a unique identifier (h3,h4 etc)
        self.isEmpty=isEmpty                          # False = sqaure is empty, True = sqaure not empty
        self.chessPiece=chessPiece('null','null','null',0)     # what chessPiece is placed on the square if its not empty
        #self.chessPiece = ''


class chessBoard: #chessBoard will contain a 2D array of square instances

    def __init__(self):
        self.array = np.ndarray((8,8),dtype=object)

    def initializeBoard(self):
        num=8
        for i in range(8):
            st='a'
            for j in range(8):
                number=str(num)            
                st=st+number
                if(num>=7 or num <=2):
                    empty=False
                else:
                    empty=True
                self.array[i][j] = square(st,empty)
                #print(self.array[i][j].chessPiece)
                
                #set colour of box
                if i % 2 == 0 and j % 2 != 0:
                    self.array[i][j].boxColour = "44m" #set dark blue bg, white text
                elif i % 2 != 0 and j % 2 == 0:
                    self.array[i][j].boxColour = "44m" #set dark blue bg, white text
                    

                st=chr(ord(st[0])+1)
            num=num-1
        self.placeChessPieces()
        #CHESSBOARD=self.array

    def placeChessPieces(self):
        
        st="a"
        for it in range(8):         #Placing Black Pawns
            
            st+=str(7)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chessPiece=Pawn("black",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st="a"
        for it in range(8):         #Placing white Pawns           
            st+=str(2)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chessPiece=Pawn("white",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st=ord('c')-ord('a')                     #Placing black Bishop(c8,f8)         
        self.array[0][st].chessPiece=Bishop("black","c8")
        st=ord('f')-ord('a')                               
        self.array[0][st].chessPiece=Bishop("black","f8")
       

        st=ord('c')-ord('a')                     #Placing white Bishop(c1,f1)            
        self.array[7][st].chessPiece=Bishop("white","c1")
        st=ord('f')-ord('a')                            
        self.array[7][st].chessPiece=Bishop("white","f1")              
                      

        st=0                    #Placing black Rook(a8,h8)         
        self.array[0][st].chessPiece=Rook("black","a8")
        st=ord('h')-ord('a')                                
        self.array[0][st].chessPiece=Rook("black","h8")
       

        st=0                    #Placing white Rook(a1,h1)            
        self.array[7][st].chessPiece=Rook("white","a1")
        st=ord('h')-ord('a')                            
        self.array[7][st].chessPiece=Rook("white","h1")     

        st=ord('b')-ord('a')                    #Placing black Knight(b8,g8)         
        self.array[0][st].chessPiece=Knight("black","b8")
        st=ord('g')-ord('a')                                
        self.array[0][st].chessPiece=Knight("black","g8")

        st=ord('b')-ord('a')                    #Placing White Knight(b8,g8)         
        self.array[7][st].chessPiece=Knight("white","b1")
        st=ord('g')-ord('a')                                
        self.array[7][st].chessPiece=Knight("white","g1")


        st=ord('d')-ord('a')                    #Placing black Queeen(d8)         
        self.array[0][st].chessPiece=Queen("black","d8")

        st=ord('e')-ord('a')                    #Placing black King(e8)         
        self.array[0][st].chessPiece=King("black","e8")


        st=ord('d')-ord('a')                    #Placing white Queeen(d1)         
        self.array[7][st].chessPiece=Queen("white","d1")

        st=ord('e')-ord('a')                    #Placing white King(e1)         
        self.array[7][st].chessPiece=King("white","e1")
        
    def moveChessPiece(self, current, destination, agent):
        cCol=ord(current[0])-ord('a')
        cRow=8-int(current[1])
        dCol=ord(destination[0])-ord('a')
        dRow=8-int(destination[1])

        if not self.array[cRow][cCol].chessPiece.checkValidMove(cRow, cCol, dRow, dCol, self.array, agent.colour):
            print("Invalid Move! checkValidMove is False")
            return False
        """ elif self.array[dRow][dCol].isEmpty==False:
            if self.array[dRow][dCol].chessPiece.colour==agent.colour:
                print("Invalid Move! Same colour at destination")
                return False """

        """ if self.array[cRow][cCol].chessPiece.pathClear(cRow, cCol, dRow, dCol, self.array, agent.colour)==False:
            print("Path not clear")
            return False """

        if self.array[dRow][dCol].isEmpty==False:                                  # if square not empty, ie. there is a piece on it
            if self.array[dRow][dCol].chessPiece.colour!=agent.colour:               # check if the piece is of opponent
                agent.attacked+=1
                agent.attackedPieces.append(self.array[dRow][dCol].chessPiece)
                agent.score+=self.array[dRow][dCol].chessPiece.strength
                self.array[dRow][dCol].chessPiece.remove()

        self.array[dRow][dCol].chessPiece=copy.deepcopy(self.array[cRow][cCol].chessPiece)
        self.array[dRow][dCol].isEmpty=False
        self.array[cRow][cCol].chessPiece.remove()
        self.array[cRow][cCol].isEmpty=True
        print(self.array[cRow][cCol].identifier+" is emptied!")
        return True

    def randomMoveChessPiece(self, agent):
        move = random.choice(self.generateMoves(agent.colour))
        print("Move\nStart: ",move.startX, ' ', move.startY, "\nEnd: ", move.endX, ' ', move.endX)
        startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
        endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX)
        while 1:
            if self.array[move.startX][move.startY].chessPiece.checkValidMove(move.startX, move.startY, move.endX, move.endY, self.array, agent.colour):
            #if startIdentifier[1] == '7':   #only choose black pawns for now
                break
            else:
                print("Another random move")
                move = random.choice(self.generateMoves(agent.colour))
            startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
            endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX)

        print("startIdentifier: ", startIdentifier)
        print("endIdentifier: ", endIdentifier)
        self.moveChessPiece(startIdentifier,endIdentifier, agent)

    def generateMoves(self, colour):
        moves = []
        moves.extend(generatePawnMoves(colour,self.array))
        moves.extend(generateBishopMoves(colour,self.array))
        moves.extend(generateRookMoves(colour,self.array))
        moves.extend(generateKnightMoves(colour,self.array))
        moves.extend(generateKingMoves(colour,self.array))
        moves.extend(generateQueenMoves(colour,self.array))
        return moves

    """ def countPieces(self, pieceName, colour):
        count=0
        for i in range(8):
            for j in range(8):
                if (self.array[i][j].state==False):
                    if(self.array[i][j].chessPiece.name==pieceName and self.array[i][j].chessPiece.colour==colour):
                        count+=1
        return count               


    def materialFunction(self):
        wp = self.countPieces('p',"white")
        bp = self.countPieces('p',"black")
        wn = self.countPieces('k',"white")
        bn = self.countPieces('k',"black")
        wb = self.countPieces('b',"white")
        bb = self.countPieces('b',"black")
        wr = self.countPieces('r',"white")
        br = self.countPieces('r',"black")
        wq = self.countPieces('Q',"white")
        bq = self.countPieces('Q',"black")

        material = 100*(wp-bp)+320*(wn-bn)+330*(wb-bb)+500*(wr-br)+900*(wq-bq)

        return material """


    def positionsFunction(self):
        evaluation=0
        for i in range(8):
            for j in range(8):
                if (self.array[i][j].isEmpty==False):
                    tempChessPiece = self.array[i][j].chessPiece
                    if tempChessPiece.name == 'pawn':
                        evaluation += tables.pawnEvalWhite[i][j] if tempChessPiece.colour == 'white' else tables.pawnEvalBlack[i][j]
                    elif tempChessPiece.name == 'bishop':
                        evaluation += tables.bishopEvalWhite[i][j] if tempChessPiece.colour == 'white' else tables.bishopEvalBlack[i][j]
                    elif tempChessPiece.name == 'rook':
                        evaluation += tables.rookEvalWhite[i][j] if tempChessPiece.colour == 'white' else tables.rookEvalBlack[i][j]
                    elif tempChessPiece.name == 'knight':
                        evaluation += tables.knightEval[i][j]
                    elif tempChessPiece.name == 'queen':
                        evaluation += tables.evalQueen[i][j]
                    elif tempChessPiece.name == 'king':
                        evaluation += tables.kingEvalWhite[i][j] if tempChessPiece.colour == 'white' else tables.kingEvalBlack[i][j]
                        #---------IMPLEMENT KING'S ENDGAME TABLE AND SCORE HERE-------#
        return evaluation


    def materialFunction(self):
            strength = 0
            for i in range(8):
                for j in range(8):
                    if self.array[i][j].isEmpty == False:
                        if self.array[i][j].chessPiece.colour == 'white':
                            strength += self.array[i][j].chessPiece.strength
                        elif self.array[i][j].chessPiece.colour == 'black':
                            strength -= self.array[i][j].chessPiece.strength
            return strength

    def evaluationFunction(self):
        #return self.materialFunction()+self.positionsFunction()
        return self.materialFunction()

    def displayChessBoard(self):
        print("Evaluation: ", self.evaluationFunction())
        for i in range(8):
            for j in range(8):
                if self.array[i][j].isEmpty==True:
                    print("\033["+self.array[i][j].textStyle+";"+self.array[i][j].textColour+";"+self.array[i][j].boxColour, self.array[i][j].identifier, end=" ")
                else:
                    print("\033["+self.array[i][j].textStyle+";"+self.array[i][j].chessPiece.colourID+";"+self.array[i][j].boxColour, self.array[i][j].chessPiece.symbol+" ", end=" ")
                    #print(self.array[i][j].boxColour, self.array[i][j].chessPiece.name+" ", end=" ")
            print("")
    
    def updateChessBoard():
        pass