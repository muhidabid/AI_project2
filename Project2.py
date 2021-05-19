import sys
import numpy as np



class square:
    def __init__(self, identifier, state):
        self.identifier=identifier      #Each square has a unique identifier (h3,h4 etc)
        self.state=state    #Tells if a sqaure is empty or not
        self.chesspiece=chessPiece('nu','null',0) #what chesspiece is placed on the square if its not empty

    

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
                st=chr(ord(st[0])+1)
            num=num-1
        self.placeChessPieces()

    def placeChessPieces(self):
        
        st="a"
        for it in range(8):         #Placing White Pawns
            
            st+=str(7)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chesspiece=Pawn("white",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st="a"
        for it in range(8):         #Placing Black Pawns           
            st+=str(2)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chesspiece=Pawn("white",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st=ord('c')-ord('a')                     #Placing White Bishop(c8,f8)         
        self.array[0][st].chesspiece=Bishop("white","c8")
        st=ord('f')-ord('a')                               
        self.array[0][st].chesspiece=Bishop("white","f8")
       

        st=ord('c')-ord('a')                     #Placing Black Bishop(c1,f1)            
        self.array[7][st].chesspiece=Bishop("black","c1")
        st=ord('f')-ord('a')                            
        self.array[7][st].chesspiece=Bishop("black","f1")              
                      

        st=0                    #Placing White Rook(a8,h8)         
        self.array[0][st].chesspiece=Rook("white","a8")
        st=ord('h')-ord('a')                                
        self.array[0][st].chesspiece=Rook("white","h8")
       

        st=0                    #Placing Black Rook(a1,h1)            
        self.array[7][st].chesspiece=Rook("black","a1")
        st=ord('h')-ord('a')                            
        self.array[7][st].chesspiece=Rook("black","h1")     

        st=ord('b')-ord('a')                    #Placing White Knight(b8,g8)         
        self.array[0][st].chesspiece=Knight("white","b8")
        st=ord('g')-ord('a')                                
        self.array[0][st].chesspiece=Knight("white","g8")

        st=ord('b')-ord('a')                    #Placing White Knight(b8,g8)         
        self.array[7][st].chesspiece=Knight("black","b1")
        st=ord('g')-ord('a')                                
        self.array[7][st].chesspiece=Knight("black","g1")


        st=ord('d')-ord('a')                    #Placing White Queeen(d8)         
        self.array[0][st].chesspiece=Queen("white","d8")

        st=ord('e')-ord('a')                    #Placing White King(e8)         
        self.array[0][st].chesspiece=King("white","e8")


        st=ord('d')-ord('a')                    #Placing Black Queeen(d1)         
        self.array[7][st].chesspiece=Queen("black","d1")

        st=ord('e')-ord('a')                    #Placing Black King(e1)         
        self.array[7][st].chesspiece=King("black","e1")
        
        


    def evaluationFunction():
        pass

    def displayChessBoard(self):
        for i in range(8):
            for j in range(8):
                if self.array[i][j].state==True:
                    print(self.array[i][j].identifier, end=" ")
                else:
                    print(self.array[i][j].chesspiece.name+" ", end=" ")
            print("")
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




board=chessBoard()
board.initializeBoard()
board.displayChessBoard()