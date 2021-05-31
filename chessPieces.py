from typing import Collection


class chessPiece:

    def __init__(self, name, symbol, colour, position, strength=0):
        self.strength=strength
        self.name=name
        self.symbol=symbol
        self.colour=colour
        self.position=position
        self.path=[] #Movement path for one turn, is used to check if it is clear or not

        #set colourID
        if colour == "black":
            self.colourID = "30"    # dark gray
        elif colour == "white":
            self.colourID = "37"    # white

    def remove(self):
        self.name="null"
        self.symbol="null"
        self.colour="null"
        self.strength=0
        
class Pawn(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'pawn','♟',colour,position,10)
        elif colour == "black":
            chessPiece.__init__(self,'pawn','♟',colour,position,-10)
         """
        chessPiece.__init__(self,'pawn','♟',colour,position,10)
        self.move=0 #Can take two steps in first move

    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):#self,currentpos,destpos,colour=None):
        #Pawn can move only forward and diagonally(if opponent gets attacked)
        
        """ if colour == 'white':
            if(ord(currentpos[0])+1==ord(destpos[0])):       #right diagonal
                if(int(currentpos[1])+1==int(destpos[1])):   
                    return True 

            if(ord(currentpos[0])-1==ord(destpos[0])):       #left diagonal
                if(int(currentpos[1])+1==int(destpos[1])):
                    return True 

            if(ord(currentpos[0])==ord(destpos[0])): #forward
                if(int(currentpos[1])+1==int(destpos[1])):
                    return True 
        
        if colour == 'black':
            if(ord(currentpos[0])+1==ord(destpos[0])):       #right diagonal
                if(int(currentpos[1])-1==int(destpos[1])):   
                    return True 

            if(ord(currentpos[0])-1==ord(destpos[0])):       #left diagonal
                if(int(currentpos[1])-1==int(destpos[1])):
                    return True 

            if(ord(currentpos[0])==ord(destpos[0])): #forward
                if(int(currentpos[1])-1==int(destpos[1])):
                    return True  """

        """ if self.colour == 'white':
                    if cRow == 6:                                   # first time moving pawn
                        if cRow-1 == dRow and cCol == dCol:         # 1 forward
                            return True
                        if cRow-2 == dRow and cCol == dCol:         # 2 forward
                            return True
                    if cRow-1 == dRow and cCol == dCol:         # forward
                        return True
                    elif cCol+1 == dCol and cRow-1 == dRow:     # right diagonal
                        return True
                    elif cCol-1 == dCol and cRow-1 == dRow:     # left diagonal
                        return True
                elif self.colour == 'black':
                    if cRow == 1:                                   # first time moving pawn
                        if cRow+1 == dRow and cCol == dCol:         # 1 forward
                            return True
                        if cRow+2 == dRow and cCol == dCol:         # 2 forward
                            return True
                    if cRow+1 == dRow and cCol == dCol:         # forward
                        return True
                    elif cCol+1 == dCol and cRow+1 == dRow:     # right diagonal
                        return True
                    elif cCol-1 == dCol and cRow+1 == dRow:     # left diagonal
                        return True """
        
        if colour == 'white':
            if cRow == 6:                                   # first time moving pawn
                if cRow-1 == dRow and cCol == dCol:         # 1 forward
                    if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, True): 
                        if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True
                if cRow-2 == dRow and cCol == dCol:         # 2 forward
                    if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, True): 
                        if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True

            if cRow-1 == dRow and cCol == dCol:         # forward
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True
            elif cCol+1 == dCol and cRow-1 == dRow:     # right diagonal
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, True, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, True): return True
            elif cCol-1 == dCol and cRow-1 == dRow:     # left diagonal
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, True, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, True): return True
        elif colour == 'black':
            if cRow == 1:                                   # first time moving pawn
                if cRow+1 == dRow and cCol == dCol:         # 1 forward
                    if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, True): 
                        if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True
                if cRow+2 == dRow and cCol == dCol:         # 2 forward
                    if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, True): 
                        if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True

            if cRow+1 == dRow and cCol == dCol:         # forward
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, False, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, False): return True
            elif cCol+1 == dCol and cRow+1 == dRow:     # right diagonal
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, True, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, True): return True
            elif cCol-1 == dCol and cRow+1 == dRow:     # left diagonal
                if self.pathClear(cRow, cCol, dRow, dCol, board, colour, True, False): 
                    if self.ifAttackCheckValid(cRow, cCol, dRow, dCol, board, colour, True): return True
        return False    #Invalid Move

    def ifAttackCheckValid(self,cRow,cCol,dRow,dCol,board,colour, isDiagonal):
        if isDiagonal:
            if board[dRow][dCol].isEmpty:
                return False            # square empty so invalid move
            elif board[dRow][dCol].chessPiece.colour != colour:
                return True             # square not empty and attackable
        else:
            if board[dRow][dCol].isEmpty:
                return True             # square empty so valid attack
            elif board[dRow][dCol].chessPiece.colour != colour:
                return True             # square not empty and attackable
        
        ##print('Invalid colour on destination')
        return False                # same colour piece so invalid
    
    def pathClear(self, cRow, cCol, dRow, dCol, board, colour, isDiagonal, isFirstMove):        
        if colour == 'white' and not isDiagonal:
            if isFirstMove:     # might be moving 2 steps
                while dRow != cRow:     # we check dRow then -- and check again until we r on cRow
                    if not board[dRow][dCol].isEmpty:       # path not clear when blocked by ANY colour on first move
                        return False
                    dRow+=1
                return True
            else:               # moving only 1 step
                if not board[dRow][dCol].isEmpty:       # path not clear when blocked by ANY colour on first move
                    return False
        elif colour == 'black' and not isDiagonal:
            if isFirstMove:     # might be moving 2 steps
                while dRow != cRow:     # we check dRow then -- and check again until we r on cRow
                    if not board[dRow][dCol].isEmpty:       # path not clear when blocked by ANY colour on first move
                        return False
                    dRow-=1
                return True
            else:               # moving only 1 step
                if not board[dRow][dCol].isEmpty:       # path not clear when blocked by ANY colour on first move
                    return False
        return True     # dont check for diagonal here, ifAttackCheckValid function checks diagonal

class Bishop(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'bishop','♝',colour,position,30)
        elif colour == "black":
            chessPiece.__init__(self,'bishop','♝',colour,position,-30) """
        chessPiece.__init__(self,'bishop','♝',colour,position,30)
        

    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):
        #Bishop can move diagonally 
        #if(abs(ord(currentpos[0])-ord(destpos[0])) == abs(int(currentpos[1])-int(destpos[1]))):                    
        
        if abs(cRow-dRow) == abs(cCol-dCol):
            ##print("Checking pathclear and attack...")
            if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):return True
        #else:#print("BISHOP FALSE MOVE")
        return False

    def pathClear(self, cRow, cCol, dRow, dCol, board, colour):
        """ cRow=int(currentpos[1])
        cCol=ord(currentpos[0])-ord('a')
        dRow=int(destpos[1])
        dCol=ord(destpos[0])-ord('a') """

        """ if(dRow<cRow and dCol>cCol):  #upper right diagonal
            cRow-=1
            cCol+=1
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print('path not clear upper right diagonal')
                    return False
                cRow-=1
                cCol+=1


        elif(dRow>cRow and dCol>cCol):  #lower right diagonal
            cRow+=1
            cCol+=1
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print('path not clear lower right diagonal')
                    return False
                cRow+=1
                cCol+=1



        elif(dRow<cRow and dCol<cCol):  #upper left diagonal
            cRow-=1
            cCol-=1
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print('path not clear upper left diagonal')
                    return False
                cRow-=1
                cCol-=1


        elif(dRow>cRow and dCol<cCol):  #lower left diagonal
            cRow+=1
            cCol-=1
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print('path not clear lower left diagonal')
                    return False
                cRow+=1
                cCol-=1 """
        if(dRow<cRow and dCol>cCol):  #upper right diagonal
            while cRow!=dRow:
                dRow+=1
                dCol-=1
                if not board[dRow][dCol].isEmpty and cRow!=dRow:
                    #print('path not clear upper right diagonal')
                    return False

        if(dRow>cRow and dCol>cCol):  #lower right diagonal
            while(cRow!=dRow):
                dRow-=1
                dCol-=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear lower right diagonal')
                    return False



        if(dRow<cRow and dCol<cCol):  #upper left diagonal
            while(cRow!=dRow):
                dRow+=1
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear upper left diagonal')
                    return False


        if(dRow>cRow and dCol<cCol):  #lower left diagonal
            while(cRow!=dRow):
                dRow-=1
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear lower left diagonal')
                    return False
                
        return True       

    def ifAttackCheckValid(self,dRow,dCol,board,colour):
        if board[dRow][dCol].isEmpty:
            return True             # square empty so valid attack
        elif board[dRow][dCol].chessPiece.colour != colour:
            return True             # square not empty and attackable
        ##print('Invalid colour on destination')
        return False                # same colour piece so invalid
        
class Rook(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'rook','♜',colour,position,50)
        elif colour == "black":
            chessPiece.__init__(self,'rook','♜',colour,position,-50)"""
        chessPiece.__init__(self,'rook','♜',colour,position,50)

    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):

        """ if(ord(currentpos[0])==ord(destpos[0])):
            return True
        if(int(currentpos[1])==int(destpos[1])):                
            return True """
        if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):
            if cRow == dRow or cCol == dCol:return True
        return False


    def pathClear(self, cRow, cCol, dRow, dCol, board, colour):
        """ cRow=int(currentpos[1])
        cCol=ord(currentpos[0])-ord('a')
        dRow=int(destpos[1])
        dCol=ord(destpos[0])-ord('a') """

        #if(ord(currentpos[0])==ord(destpos[0]) and cRow<dRow ): #forward
        """ if cCol==dCol and cRow>dRow: #upward
            cRow-=1
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print(cRow,cCol, board[7-cRow][cCol].isEmpty)
                    ##print(dRow,dCol, board[7-dRow][dCol].isEmpty)
                    ##print("Path not clear/Invalid move!")
                    return False
                cRow-=1
                

        if cCol==dCol and cRow<dRow: #downward
            cRow+=1 
            while(cRow!=dRow):
                if(board[cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move!")
                    return False
                cRow+=1


        if cCol<dCol and cRow==dRow: #right
            cCol+=1
            while(cCol!=dCol):
                if(board[cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move!")
                    return False
                cCol+=1

        if cCol>dCol and cRow==dRow: #left
            cCol-=1
            while(cCol!=dCol):
                if(board[cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move1!")
                    return False
                cCol-=1 """
        if cCol==dCol and cRow>dRow: #upward
            while(cRow!=dRow):
                dRow+=1
                if board[dRow][dCol].isEmpty==False and cRow!=dRow:
                    ##print(cRow,cCol, board[7-cRow][cCol].isEmpty)
                    ##print(dRow,dCol, board[7-dRow][dCol].isEmpty)
                    #print("Path not clear upward")
                    return False
                

        if cCol==dCol and cRow<dRow: #downward
            while(cRow!=dRow):
                dRow-=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print("Path not clear downward")
                    return False


        if cCol<dCol and cRow==dRow: #right
            while(cCol!=dCol):
                dCol-=1
                if(board[dRow][dCol].isEmpty==False) and cCol!=dCol:
                    #print("Path not clear right")
                    return False

        if cCol>dCol and cRow==dRow: #left
            while(cCol!=dCol):
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cCol!=dCol:
                    #print("Path not clear left")
                    return False

        return True

    def ifAttackCheckValid(self,dRow,dCol,board,colour):
        if board[dRow][dCol].isEmpty:
            return True             # square empty so valid attack
        elif board[dRow][dCol].chessPiece.colour != colour:
            return True             # square not empty and attackable
        ##print('Invalid colour on destination')
        return False                # same colour piece so invalid

class Knight(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'knight','♞',colour,position,30)
        elif colour == "black":
            chessPiece.__init__(self,'knight','♞',colour,position,-30)"""
        chessPiece.__init__(self,'knight','♞',colour,position,30)
    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):

        """ if(ord(currentpos[0])+1==ord(destpos[0])):       
            if(int(currentpos[1])+2==int(destpos[1]) or int(currentpos[1])-2==int(destpos[1]) ):                
                return True
        if(ord(currentpos[0])-1==ord(destpos[0])):       
            if(int(currentpos[1])+2==int(destpos[1]) or int(currentpos[1])-2==int(destpos[1]) ):                
                return True   """

        if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):
            if cRow-2>=0 and cCol+1<=7: 
                if cRow-2 ==dRow and cCol+1 ==dCol:return True
            if cRow-1>=0 and cCol+2<=7: 
                if cRow-1 ==dRow and cCol+2 ==dCol:return True
            if cRow+1<=7 and cCol+2<=7: 
                if cRow+1 ==dRow and cCol+2 ==dCol:return True
            if cRow+2<=7 and cCol+1<=7: 
                if cRow+2 ==dRow and cCol+1 ==dCol:return True
            # left half of moves
            if cRow+2<=7 and cCol-1>=0: 
                if cRow+2 ==dRow and cCol-1 ==dCol:return True
            if cRow+1<=7 and cCol-2>=0: 
                if cRow+1 ==dRow and cCol-2 ==dCol:return True
            if cRow-1>=0 and cCol-2>=0: 
                if cRow-1 ==dRow and cCol-2 ==dCol:return True
            if cRow-2>=0 and cCol-1>=0: 
                if cRow-2 ==dRow and cCol-1 ==dCol:return True
        #else:#print("Path not clear")        
        return False    #Invalid Move
    
    def pathClear(self, cRow, cCol, dRow, dCol, board, colour):
        return True

    def ifAttackCheckValid(self,dRow,dCol,board,colour):
        if board[dRow][dCol].isEmpty:
            return True             # square empty so valid attack
        elif board[dRow][dCol].chessPiece.colour != colour:
            return True             # square not empty and attackable
        ##print('Invalid colour on destination')
        return False                # same colour piece so invalid

class Queen(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'queen','♛',colour,position,90)
        elif colour == "black":
            chessPiece.__init__(self,'queen','♛',colour,position,-90) """
        chessPiece.__init__(self,'queen','♛',colour,position,90)

    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):

        """ if(ord(currentpos[0])==ord(destpos[0])):      
            return True
        if(int(currentpos[1])==int(destpos[1])):                
            return True
        if(abs(ord(currentpos[0])-ord(destpos[0])) == abs(int(currentpos[1])-int(destpos[1]))):                    
            return True """
        if cRow==dRow:
            if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):return True
        elif cCol==dCol:
            if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):return True
        elif abs(cRow-dRow) == abs(cCol-dCol):
            if self.pathClear(cRow, cCol, dRow, dCol, board, colour) and self.ifAttackCheckValid(dRow,dCol,board,colour):return True
        #else:#print("QUEEN Path not clear")
        return False

    def pathClear(self, cRow, cCol, dRow, dCol, board, colour):
        """ 
        if(dRow>cRow and dCol>cCol):  #upper right diagonal
            cRow+=1
            cCol+=1
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move1!")
                    return False
                cRow+=1
                cCol+=1
            return True

        if(dRow<cRow and dCol>cCol):  #lower right diagonal
            cRow-=1
            cCol+=1
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move2!")
                    return False
                cRow-=1
                cCol+=1
            return True


        if(dRow>cRow and dCol<cCol):  #upper left diagonal
            cRow+=1
            cCol-=1
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move3!")
                    return False
                cRow+=1
                cCol-=1
            return True

        if(dRow<cRow and dCol<cCol):  #lower left diagonal
            cRow+=1
            cCol-=1
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move4!")
                    return False
                cRow-=1
                cCol-=1
            return True

        if cCol==dCol and cRow<dRow: #forward
            cRow+=1
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print(cRow,cCol, board[7-cRow][cCol].isEmpty)
                    ##print(dRow,dCol, board[7-dRow][dCol].isEmpty)
                    ##print("Path not clear/Invalid move5!")
                    return False
                cRow+=1
            return True   

        if cCol==dCol and cRow>dRow: #backward
            cRow-=1 
            while(cRow!=dRow):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move6!")
                    return False
                cRow-=1
            return True

        if(cCol<dCol and cRow==dRow ): #right
            cCol+=1
            while(cCol!=dCol):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move7!")
                    return False
                cCol+=1
            return True

        if cCol>dCol and cRow==dRow: #left
            cCol-=1
            while(cCol!=dCol):
                if(board[7-cRow][cCol].isEmpty==False):
                    ##print("Path not clear/Invalid move!")
                    return False
                cCol-=1
            return True
 """
        if(dRow<cRow and dCol>cCol):  #upper right diagonal
            while cRow!=dRow:
                dRow+=1
                dCol-=1
                if not board[dRow][dCol].isEmpty and cRow!=dRow:
                    #print('path not clear upper right diagonal')
                    return False

        if(dRow>cRow and dCol>cCol):  #lower right diagonal
            while(cRow!=dRow):
                dRow-=1
                dCol-=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear lower right diagonal')
                    return False



        if(dRow<cRow and dCol<cCol):  #upper left diagonal
            while(cRow!=dRow):
                dRow+=1
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear upper left diagonal')
                    return False


        if(dRow>cRow and dCol<cCol):  #lower left diagonal
            while(cRow!=dRow):
                dRow-=1
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print('path not clear lower left diagonal')
                    return False

        if cCol==dCol and cRow>dRow: #upward
            while(cRow!=dRow):
                dRow+=1
                if board[dRow][dCol].isEmpty==False and cRow!=dRow:
                    ##print(cRow,cCol, board[7-cRow][cCol].isEmpty)
                    ##print(dRow,dCol, board[7-dRow][dCol].isEmpty)
                    #print("Path not clear upward")
                    return False
                

        if cCol==dCol and cRow<dRow: #downward
            while(cRow!=dRow):
                dRow-=1
                if(board[dRow][dCol].isEmpty==False) and cRow!=dRow:
                    #print("Path not clear downward")
                    return False


        if cCol<dCol and cRow==dRow: #right
            while(cCol!=dCol):
                dCol-=1
                if(board[dRow][dCol].isEmpty==False) and cCol!=dCol:
                    #print("Path not clear right")
                    return False

        if cCol>dCol and cRow==dRow: #left
            while(cCol!=dCol):
                dCol+=1
                if(board[dRow][dCol].isEmpty==False) and cCol!=dCol:
                    #print("Path not clear left")
                    return False
        return True

    def ifAttackCheckValid(self,dRow,dCol,board,colour):
        if board[dRow][dCol].isEmpty:
            #print('ifAttack 1 True')
            return True             # square empty so valid attack
        elif board[dRow][dCol].chessPiece.colour != colour:
            #print('ifAttack 2 True')
            return True             # square not empty and attackable
        ##print('Invalid colour on destination')
        #print('ifAttack 3 False')
        return False                # same colour piece so invalid
                
class King(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'king','♚',colour,position,900)
        elif colour == "black":
            chessPiece.__init__(self,'king','♚',colour,position,-900) """
        chessPiece.__init__(self,'king','♚',colour,position,900)

    def checkValidMove(self, cRow, cCol, dRow, dCol, board, colour):
        """ if(ord(currentpos[0])+1==ord(destpos[0])):       #right diagonal
                if(int(currentpos[1])+1==int(destpos[1]) or int(currentpos[1])-1==int(destpos[1])):            
                    return True 
        
        if(ord(currentpos[0])-1==ord(destpos[0])):       #left diagonal
            if(int(currentpos[1])+1==int(destpos[1]) or int(currentpos[1])-1==int(destpos[1])):
                return True 
            
        if(ord(currentpos[0])==ord(destpos[0])): #forward/backwards
            if(int(currentpos[1])+1==int(destpos[1]) or int(currentpos[1])-1==int(destpos[1])):
                return True
            
        if(int(currentpos[1])==int(destpos[1])): #sideways
            if(ord(currentpos[0])-1==ord(destpos[0]) or ord(currentpos[0])+1==ord(destpos[0])):
                return True """

        if self.ifAttackCheckValid(dRow,dCol,board,colour):    
            if cCol+1==dCol:    #right diagonal
                if cRow+1==dRow or cRow-1==dRow:return True
            if cCol-1==dCol:    #left diagonal
                if cRow+1==dRow or cRow-1==dRow:return True
            if cCol==dCol:      #forward/backward
                if cRow+1==dRow or cRow-1==dRow:return True
            if cRow==dRow:      #sideways
                if cCol-1==dCol or cCol+1==dCol:return True
        #else:#print("Path not clear")        
        return False    #Invalid Move

    def pathClear(self, cRow, cCol, dRow, dCol, board, colour):
        # king can only move one step so ifAttackCheckValid checks path too
        return True
    
    def ifAttackCheckValid(self,dRow,dCol,board,colour):
        if board[dRow][dCol].isEmpty:
            return True             # square empty so valid attack
        elif board[dRow][dCol].chessPiece.colour != colour:
            return True             # square not empty and attackable
        ##print('Invalid colour on destination')
        return False                # same colour piece so invalid