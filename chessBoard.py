import numpy as np
import copy
import random
from numpy import inf
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

class prevBeatChessPiece:
    def __init__(self,cRow,cCol,dRow,dCol,chessPiece):
        self.fromThisX=cRow
        self.fromThisY=cCol
        self.atThisX=dRow
        self.atThisY=dCol
        self.chessPiece=chessPiece

class chessBoard: #chessBoard will contain a 2D array of square instances

    def __init__(self):
        self.gamePhase = 'starting'
        self.whiteMaterial = 0
        self.blackMaterial = 0
        self.noOfMovesHistory = 0
        self.blackQueenSideCastling = {'right':True, 'left':True}
        self.blackKingSideCastling = True
        self.whiteQueenSideCastling = {'right':True, 'left':True}
        self.whiteKingSideCastling = True
        
        """ self.history = []
        self.whiteNumOfMoves = 0
        self.blackNumOfMoves = 0 """

        self.array = np.ndarray((8,8),dtype=object)
        self.prevBoardState = np.ndarray((8,8),dtype=object)
        self.prevBeatChessPiece = prevBeatChessPiece(0,0,0,0,chessPiece('null','null','null',0))
        self.bestMove=Move(0,0,0,0)
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
                self.prevBoardState[i][j] = square(st,empty)

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
    #-----------------------------Movement-----------------------------------    
    def moveChessPiece(self, current, destination, agent):
        cCol=ord(current[0])-ord('a')
        cRow=8-int(current[1])
        dCol=ord(destination[0])-ord('a')
        dRow=8-int(destination[1])
        pieceToMove = self.array[cRow][cCol].chessPiece
        #print('cRow: ',cRow,'\ncCol: ',cCol,'\ndRow: ',dRow,'\ndCol: ',dCol)

        if cRow not in range(8) and cCol not in range(8) and dRow not in range(8) and dCol not in range(8):
            return False
        
        # -------- ! CASTLING ! ------- #
        if pieceToMove.name=='king':
            isCastling, direction = self.castling(cRow, cCol, dRow, dCol, self.array, agent.colour, pieceToMove)  # checks both rook and king conditions
            if isCastling:
                self.forceMoveChessPiece(current, destination, agent)       # move king

                if direction == 'whiteRight':
                    self.forceMoveChessPiece('h1', 'f1', agent)   # move bottom right rook
                    self.whiteQueenSideCastling['right'] = False
                    self.whiteKingSideCastling = False
                elif direction == 'whiteLeft':
                    self.forceMoveChessPiece('a1', 'd1', agent)   # move bottom left rook
                    self.whiteQueenSideCastling['left'] = False
                    self.whiteKingSideCastling = False
                elif direction == 'blackRight':
                    self.forceMoveChessPiece('h8', 'f8', agent)   # move top right rook
                    self.blackQueenSideCastling['right'] = False
                    self.blackKingSideCastling = False
                elif direction == 'blackLeft':
                    self.forceMoveChessPiece('a8', 'd8', agent)   # move top left rook
                    self.blackQueenSideCastling['left'] = False
                    self.blackKingSideCastling = False
                
                return True
                
            
        if not pieceToMove.checkValidMove(cRow, cCol, dRow, dCol, self.array, agent.colour):
            #print("Invalid Move! checkValidMove is False")
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
                ###self.prevBeatChessPiece = prevBeatChessPiece(cRow,cCol,dRow,dCol,chessPiece(self.array[dRow][dCol].chessPiece.name,self.array[dRow][dCol].chessPiece.symbol,self.array[dRow][dCol].chessPiece.colour,0))
                agent.attackedPieces.append(self.array[dRow][dCol].chessPiece)
                agent.score+=self.array[dRow][dCol].chessPiece.strength
                self.array[dRow][dCol].chessPiece.remove()

        self.array[dRow][dCol].chessPiece=copy.deepcopy(pieceToMove)
        self.array[dRow][dCol].isEmpty=False
        pieceToMove.remove()
        self.array[cRow][cCol].isEmpty=True
        #print(self.array[cRow][cCol].identifier+" is emptied!")
        
        return True

    def forceMoveChessPiece(self, current, destination, agent):
        cCol=ord(current[0])-ord('a')
        cRow=8-int(current[1])
        dCol=ord(destination[0])-ord('a')
        dRow=8-int(destination[1])
        #print('cRow: ',cRow,'\ncCol: ',cCol,'\ndRow: ',dRow,'\ndCol: ',dCol)

        """ if self.array[dRow][dCol].isEmpty==False:                                  # if square not empty, ie. there is a piece on it
            if self.array[dRow][dCol].chessPiece.colour!=agent.colour:               # check if the piece is of opponent
                agent.attacked+=1
                agent.attackedPieces.append(self.array[dRow][dCol].chessPiece)
                agent.score+=self.array[dRow][dCol].chessPiece.strength
                self.array[dRow][dCol].chessPiece.remove() """

        self.array[dRow][dCol].chessPiece=copy.deepcopy(self.array[cRow][cCol].chessPiece)
        self.array[dRow][dCol].isEmpty=False
        self.array[cRow][cCol].chessPiece.remove()
        self.array[cRow][cCol].isEmpty=True
        # restore previously beat chess piece:
        ###self.array[self.prevBeatChessPiece.atThisX][self.prevBeatChessPiece.atThisY].chessPiece = self.prevBeatChessPiece.chessPiece
        #print(self.array[cRow][cCol].identifier+" is emptied!")
        return True

    def randomMoveChessPiece(self, currentAgent, opponentAgent):
        #move = random.choice(self.generateMoves(currentAgent))
        legalMoves = self.generateLegalMoves(currentAgent, opponentAgent)  
      
        """ if currentAgent.colour == 'black':
            self.blackNumOfMoves = len(legalMoves)
        elif currentAgent.colour == 'white':
            self.whiteNumOfMoves = len(legalMoves) """      
        
        move = random.choice(legalMoves)
        #self.history.append(Move(move.startX, move.startY, move.endX, move.endY))        
        startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
        endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX)
        """ print("Move\nStart: ",move.startX, ' ', move.startY, "\nEnd: ", move.endX, ' ', move.endY)
        while 1:
            if self.array[move.startX][move.startY].chessPiece.checkValidMove(move.startX, move.startY, move.endX, move.endY, self.array, agent.colour):
            #if startIdentifier[1] == '7':   #only choose black pawns for now
                break
            else:
                print("Another random move")
                move = random.choice(self.generateMoves(agent.colour))
            startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
            endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX) """

        print("startIdentifier: ", startIdentifier)
        print("endIdentifier: ", endIdentifier)
        self.moveChessPiece(startIdentifier,endIdentifier, currentAgent)

    def generateLegalMoves(self, currentAgent, opponentAgent):   # moves that dont make king open to attack in next move
        suedoLegalMoves = self.generateMoves(currentAgent)
        legalMoves = []
        for suedoLegalMove in suedoLegalMoves:  #bot's legal moves
            #print("Making move...\nStart: ",suedoLegalMove.startX, ' ', suedoLegalMove.startY, "\nEnd: ", suedoLegalMove.endX, ' ', suedoLegalMove.endY)
            self.prevBoardState = copy.deepcopy(self.array)     # STORE BOARD STATE
            self.makeMove(suedoLegalMove,currentAgent)
            opponentResponses = self.generateMoves(opponentAgent)

            for opponentResponse in opponentResponses:
                if self.isHittingKingOfAgent(opponentResponse,currentAgent):
                    #print('not legal')
                    pass
                else:
                    #print('legal')
                    
                    if suedoLegalMove not in legalMoves:
                        legalMoves.append(suedoLegalMove)
                      #  print(suedoLegalMove.startX,suedoLegalMove.startY, suedoLegalMove.endX, suedoLegalMove.endY)

            #print("Unaking move...\nStart: ",suedoLegalMove.startX, ' ', suedoLegalMove.startY, "\nEnd: ", suedoLegalMove.endX, ' ', suedoLegalMove.endY)
            #self.unmakeMove(suedoLegalMove,currentAgent)
            self.array = copy.deepcopy(self.prevBoardState)     # UNMAKE MOVE
        return legalMoves

    def minmax(self,currentAgent,opponentAgent,maximizingPlayer,currentDepth):
          

        if currentDepth == 0: #game over function call
         #   print("here:")
          #  self.displayChessBoard()
          #  print(self.bestMove.startX, self.bestMove.startY, self.bestMove.endX, self.bestMove.endY)
            return self.evaluationFunction(), self.bestMove

      
        
        if maximizingPlayer==False:
            # min player's turn
            Moves=self.generateLegalMoves(opponentAgent, currentAgent)
    #     self.displayChessBoard()
            minEval=inf
            minBoards=[]
            mov=Moves[0]
            m=minIndex=0
            newBoard=chessBoard()
        #    newBoard=chessBoard()
            for i in Moves:
            
            #    newBoard=chessBoard()
                newBoard.array=copy.deepcopy(self.array)
        #     minBoards.append(newBoard)
    #           newBoard.array[i.startX][i.startY].isEmpty=True
    #           newBoard.array[i.endX][i.endY].isEmpty=False
                startIdentifier = chr(ord('a') + i.startY) + str(8 - i.startX) 
                endIdentifier = chr(ord('a') + i.endY) + str(8 - i.endX)         
                newBoard.moveChessPiece(startIdentifier,endIdentifier,opponentAgent) 
            #   newBoard.displayChessBoard()
        #       newBoard.displayChessBoard() 
                value, newBoard.bestMove= newBoard.minmax(currentAgent,opponentAgent,True,currentDepth-1)
                value=newBoard.evaluationFunction()          
            #   newBoard.displayChessBoard()
                if value<minEval:
                    minEval=value
                    mov=i
                    minIndex=m
                m+=1
            # self.array=copy.deepcopy(newBoard.array)
    #     newBoard=minBoards[minIndex]
                
    #     self.bestMove=copy.deepcopy(move)

        #   newBoard.displayChessBoard()
    #       self.bestMove=newBoard.minmax(opponentAgent,currentAgent,currentDepth)
            newBoard.bestMove=mov
            return minEval,mov
        
        else:
            # max player's turn
            Moves=self.generateLegalMoves(currentAgent, opponentAgent)
            maxEval=-inf
            maxBoards=[]
            mov=Moves[0]
            m=maxIndex=0
            newBoard=chessBoard()
            
    #     newBoard.array=copy.deepcopy(self.array)
            for i in Moves:
            
            #   print(i.startX, i.startY, i.endX, i.endY)
                
                newBoard.array=copy.deepcopy(self.array)
            #    maxBoards.append(newBoard)
    #           newBoard.array[i.startX][i.startY].isEmpty=True
    #           newBoard.array[i.endX][i.endY].isEmpty=False
                startIdentifier = chr(ord('a') + i.startY) + str(8 - i.startX) 
                endIdentifier = chr(ord('a') + i.endY) + str(8 - i.endX)         
                newBoard.moveChessPiece(startIdentifier,endIdentifier,currentAgent)
                value, newBoard.bestMove= newBoard.minmax(currentAgent,opponentAgent,False,currentDepth-1)
        #        value=newBoard.evaluationFunction() 
        #        print(value)         
        #     newBoard.displayChessBoard()
                if value>maxEval:
                    maxEval=value
                    mov=i
                    maxIndex=m
                m+=1
        
        #    newBoard=maxBoards[maxIndex]
    #     newBoard.displayChessBoard()
        #    self.bestMove=newBoard.minmax(opponentAgent,currentAgent,currentDepth)
            newBoard.bestMove=mov
            return maxEval,mov
                
     
    def generateMoves(self, agent):
        #print('\nGenerating moves...')
        moves = []
        moves.extend(generatePawnMoves(agent.colour,self.array))
        moves.extend(generateBishopMoves(agent.colour,self.array))
        moves.extend(generateRookMoves(agent.colour,self.array))
        moves.extend(generateKnightMoves(agent.colour,self.array))
        moves.extend(generateKingMoves(agent.colour,self.array))
        moves.extend(generateQueenMoves(agent.colour,self.array))
        return moves
    #-----------------------------Evaluation------------------------------------    
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
                        if tempChessPiece.colour == 'white': 
                            evaluation += tables.pawnEvalWhite[i][j]  
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.pawnEvalWhite[i][j], end='')
                        else: 
                            evaluation -= tables.pawnEvalBlack[i][j]
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.pawnEvalBlack[i][j], end='')
                        #print('\ti: ', i, 'j: ', j)
                    elif tempChessPiece.name == 'bishop':
                        if tempChessPiece.colour == 'white': 
                            evaluation += tables.bishopEvalWhite[i][j]  
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.bishopEvalWhite[i][j], end='')
                        else: 
                            evaluation -= tables.bishopEvalBlack[i][j]
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.bishopEvalBlack[i][j], end='')
                        #print('\ti: ', i, 'j: ', j)
                    elif tempChessPiece.name == 'rook':
                        if tempChessPiece.colour == 'white': 
                            evaluation += tables.rookEvalWhite[i][j]  
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.rookEvalWhite[i][j], end='')
                        else: 
                            evaluation -= tables.rookEvalBlack[i][j]
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.rookEvalBlack[i][j], end='')
                        #print('\ti: ', i, 'j: ', j)
                    elif tempChessPiece.name == 'knight':
                        if tempChessPiece.colour == 'white': 
                            evaluation += tables.knightEvalWhite[i][j] 
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.knightEvalWhite[i][j], end='')
                        else: 
                            evaluation -= tables.knightEvalBlack[i][j]
                            #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.knightEvalBlack[i][j], end='')
                        #print('\ti: ', i, 'j: ', j)
                    elif tempChessPiece.name == 'queen':
                        if tempChessPiece.colour == 'white': 
                            evaluation += tables.queenEvalWhite[i][j]
                        else:
                            evaluation -= tables.queenEvalBlack[i][j]
                        #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.evalQueen[i][j], end='')
                        #print('\ti: ', i, 'j: ', j)
                    elif tempChessPiece.name == 'king':
                        if self.gamePhase == 'starting':
                            if tempChessPiece.colour == 'white': 
                                evaluation += tables.kingEvalWhite[i][j] 
                                #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.kingEvalWhite[i][j], end='')
                            else: 
                                evaluation -= tables.kingEvalBlack[i][j]
                                #print(tempChessPiece.name, ' ', tempChessPiece.colour, ' ', tables.kingEvalBlack[i][j], end='')
                            #print('\ti: ', i, 'j: ', j)
                        else:
                            if tempChessPiece.colour == 'white': 
                                evaluation += tables.kingWhiteEndgame[i][j]
                            else: 
                                evaluation -= tables.kingBlackEndgame[i][j]
                        # #---------IMPLEMENT KING'S ENDGAME TABLE AND SCORE HERE-------#
        return evaluation

    def materialFunction(self):
            whiteMaterial = 0
            blackMaterial = 0
            strength = 0
            for i in range(8):
                for j in range(8):
                    if self.array[i][j].isEmpty == False:
                        if self.array[i][j].chessPiece.colour == 'white':
                            strength += self.array[i][j].chessPiece.strength
                            whiteMaterial += 1
                        elif self.array[i][j].chessPiece.colour == 'black':
                            strength -= self.array[i][j].chessPiece.strength
                            blackMaterial += 1
            self.whiteMaterial = whiteMaterial
            self.blackMaterial = blackMaterial
            return strength

    def evaluationFunction(self):
        self.updateGamePhase()
        return self.materialFunction()+self.positionsFunction()
        #return self.materialFunction()
    #------------------------------King/Winning-----------------------------------    
    def isHittingKingOfAgent(self, move, agent):
        return self.array[move.endX][move.endY].chessPiece.name == 'king' and self.array[move.endX][move.endY].chessPiece.colour == agent.colour

    def checkWinning(self, agent1, agent2):
        # CHECK FOR CHECKMATE
        if len(self.generateLegalMoves(agent1,agent2))==0: 
            print(agent1.colour, ' has won by CHECKMATE!')
            return False # stop game
        elif len(self.generateLegalMoves(agent2,agent1))==0: 
            print(agent2.colour, ' has won by CHECKMATE!')
            return False # stop game
        # CHECK IF KING GOT BEAT
        whiteKing = False
        blackKing = False
        for i in range(8):
            for j in range(8):
                if not self.array[i][j].isEmpty:
                    if self.array[i][j].chessPiece.name=='king' and self.array[i][j].chessPiece.colour=='white':whiteKing=True
                    if self.array[i][j].chessPiece.name=='king' and self.array[i][j].chessPiece.colour=='black':blackKing=True
        if whiteKing==False:
            print('\n!!!Black won!!!\n')
            return False
        if blackKing==False:
            print('\n!!!White won!!!\n')
            return False
        
        return True

    def updateGamePhase(self):
        if self.noOfMovesHistory > 40 or (self.whiteMaterial < 14 and self.blackMaterial < 14):
            self.gamePhase = 'ending'  
    #------------------------------Special moves-----------------------------------    
    def checkPawnPromotion(self):
        for col in range(8):
            # check white pawns
            while 1:
                validChoice = False
                if self.array[0][col].chessPiece.name == 'pawn' and self.array[0][col].chessPiece.colour == 'white':
                    identifier = chr(ord('a') + col) + '8' 
                    print('White pawn at: ', identifier)
                    print('What do you want the pawn to promote to?')
                    choice = input('1.knight\n2.bishop\n3.rook\n4.queen\nType name of choice in lower case: ')
                    if choice=='knight' or choice=='bishop' or choice=='rook' or choice=='queen':
                        validChoice = True
                    else:
                        print("Invalid choice. Choose again...")
                else:break
                if validChoice:
                    if choice=='knight':
                        self.array[0][col].chessPiece = Knight('white',0)
                    elif choice=='bishop': 
                        self.array[0][col].chessPiece = Bishop('white',0)
                    elif choice=='rook':
                        self.array[0][col].chessPiece = Rook('white',0)
                    elif choice=='queen':
                        self.array[0][col].chessPiece = Queen('white',0)
                    self.displayChessBoard()
                    break


            # check black pawns
            # black is AI sooo the smartest thing to do is to change the pawn into a queen
            # so instead of asking or randomly choosing promotion, we will promote to a queen
            while 1:
                validChoice = False
                if self.array[7][col].chessPiece.name == 'pawn' and self.array[0][col].chessPiece.colour == 'black':
                    validChoice = True
                else:break
                if validChoice:
                    self.array[7][col].chessPiece = Queen('black',0)
                    self.displayChessBoard()
                    break

    def castling(self, cRow, cCol, dRow, dCol, board, colour, kingPiece):
        if colour == 'white':                               # colour
            if cRow == 7 and cCol == 4:                     # current index
                if dRow == 7 and dCol == 6:                 # right destination index
                    if self.whiteKingSideCastling == True and self.whiteQueenSideCastling['right'] == True:
                        if kingPiece.castlingPathClear(cRow, cCol, dRow, dCol, board, colour): return True, 'whiteRight'
                elif dRow == 7 and dCol == 2:                 # left destination index
                    if self.whiteKingSideCastling == True and self.whiteQueenSideCastling['left'] == True:
                        if kingPiece.castlingPathClear(cRow, cCol, dRow, dCol, board, colour): return True, 'whiteLeft'
        elif colour == 'black':                             # colour
            if cRow == 0 and cCol == 4:                     # current index
                if dRow == 0 and dCol == 6:                 # right destination index
                    if self.blackKingSideCastling == True and self.blackQueenSideCastling['right'] == True:
                        if kingPiece.castlingPathClear(cRow, cCol, dRow, dCol, board, colour): return True, 'blackRight'
                if dRow == 0 and dCol == 2:                 # left destination index
                    if self.blackKingSideCastling == True and self.blackQueenSideCastling['left'] == True:
                        if kingPiece.castlingPathClear(cRow, cCol, dRow, dCol, board, colour): return True, 'blackLeft'
        return False, 'False'
    #-----------------------------Supportive------------------------------------
    def makeMove(self, move, agent):
        startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
        endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX)
        return self.forceMoveChessPiece(startIdentifier,endIdentifier,agent)

    def unmakeMove(self, move, agent):
        startIdentifier = chr(ord('a') + move.startY) + str(8 - move.startX) 
        endIdentifier = chr(ord('a') + move.endY) + str(8 - move.endX)
        return self.forceMoveChessPiece(endIdentifier,startIdentifier,agent)
        #self.array = np.copy(self.prevBoardState)

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