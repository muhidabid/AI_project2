import numpy as np
import copy

import tables
from  chessPieces import *
""" from  chessPieces import Bishop
from  chessPieces import Rook
from  chessPieces import Knight
from  chessPieces import Queen
from  chessPieces import King """

class square:
    def __init__(self, identifier, isEmpty):
        #self.boxColour="\033[1;30;47m"
        self.textStyle="1"      # bold by default
        self.textColour="33"    # yellow by default
        self.boxColour="46m"    # white by default
        

        self.identifier=identifier                      # Each square has a unique identifier (h3,h4 etc)
        self.isEmpty=isEmpty                          # False = sqaure is empty, True = sqaure not empty
        #self.chessPiece=chessPiece('null','null','null',0)     # what chessPiece is placed on the square if its not empty
        self.chessPiece = ''

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
        st=ord(current[0])-ord('a')
        row=8-int(current[1])
        dst=ord(destination[0])-ord('a')
        drow=8-int(destination[1])
        valid=self.array[row][st].chessPiece.checkValidMove(current,destination)
        if valid==False:
            print("Invalid Move!")
            return 
        elif self.array[drow][dst].isEmpty==False:
            if self.array[drow][dst].chessPiece.colour==agent.colour:
                print("Invalid Move!")
                return 

        if self.array[row][st].chessPiece.pathClear(current,destination,self.array, agent)==False:
            print("Path not clear")
            return

    

        if self.array[drow][dst].isEmpty==False:                                  # if square not empty, ie. there is a piece on it
            if self.array[drow][dst].chessPiece.colour!=agent.colour:               # check if the piece is of opponent
                agent.attacked+=1
                agent.attackedPieces.append(self.array[drow][dst].chessPiece)
                agent.score+=self.array[drow][dst].chessPiece.strength
                self.array[drow][dst].chessPiece.remove()

        self.array[drow][dst].chessPiece=copy.deepcopy(self.array[row][st].chessPiece)
        self.array[drow][dst].isEmpty=False
        self.array[row][st].chessPiece.remove()
        self.array[row][st].isEmpty=True
        print(self.array[row][st].identifier+" is emptied!")



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