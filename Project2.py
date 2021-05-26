import sys
import numpy as np
import copy



CHESSBOARD= np.ndarray((8,8),dtype=object)

pawnTable=[[0,  0,  0,  0,  0,  0,  0,  0],
           [50, 50, 50, 50, 50, 50, 50, 50],
           [10, 10, 20, 30, 30, 20, 10, 10],
           [5,  5, 10, 25, 25, 10,  5,  5],
           [0,  0,  0, 20, 20,  0,  0,  0],
           [5, -5,-10,  0,  0,-10, -5,  5],
           [5, 10, 10,-20,-20, 10, 10,  5],
           [0,  0,  0,  0,  0,  0,  0,  0]]

knightTable=[[-50,-40,-30,-30,-30,-30,-40,-50],
             [-40,-20,  0,  0,  0,  0,-20,-40],
             [-30,  0, 10, 15, 15, 10,  0,-30],
             [-30,  5, 15, 20, 20, 15,  5,-30],
             [-30,  0, 15, 20, 20, 15,  0,-30],
             [-30,  5, 10, 15, 15, 10,  5,-30],
             [-40,-20,  0,  5,  5,  0,-20,-40],
             [-50,-40,-30,-30,-30,-30,-40,-50]]

bishopTable=[[-20,-10,-10,-10,-10,-10,-10,-20],
             [-10,  0,  0,  0,  0,  0,  0,-10],
             [-10,  0,  5, 10, 10,  5,  0,-10],
             [-10,  5,  5, 10, 10,  5,  5,-10],
             [-10,  0, 10, 10, 10, 10,  0,-10],
             [-10, 10, 10, 10, 10, 10, 10,-10],
             [-10,  5,  0,  0,  0,  0,  5,-10],
             [-20,-10,-10,-10,-10,-10,-10,-20]]

rookTable=[[0,  0,  0,  0,  0,  0,  0,  0],
           [5, 10, 10, 10, 10, 10, 10,  5], 
           [-5,  0,  0,  0,  0,  0,  0, -5],
           [-5,  0,  0,  0,  0,  0,  0, -5],
           [-5,  0,  0,  0,  0,  0,  0, -5],
           [-5,  0,  0,  0,  0,  0,  0, -5],
           [-5,  0,  0,  0,  0,  0,  0, -5],
           [0,  0,  0,  5,  5,  0,  0,  0 ]]     

queenTable=[[-20,-10,-10, -5, -5,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5,  5,  5,  5,  0,-10],
            [-5,  0,  5,  5,  5,  5,  0, -5],
            [0,  0,  5,  5,  5,  5,  0, -5],
            [-10,  5,  5,  5,  5,  5,  0,-10],
            [-10,  0,  5,  0,  0,  0,  0,-10],
            [-20,-10,-10, -5, -5,-10,-10,-20]]    



class square:
    def __init__(self, identifier, state):
        #self.boxColour="\033[1;30;47m"
        self.textStyle="1"      # bold by default
        self.textColour="33"    # yellow by default
        self.boxColour="46m"    # white by default
        

        self.identifier=identifier      #Each square has a unique identifier (h3,h4 etc)
        self.state=state    #Tells if a sqaure is empty or not (False==Not empty)
        self.chesspiece=chessPiece('null','null',0) #what chesspiece is placed on the square if its not empty

    

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
                
                #set color of box
                if i % 2 == 0 and j % 2 != 0:
                    self.array[i][j].boxColour = "44m" #set dark blue bg, white text
                elif i % 2 != 0 and j % 2 == 0:
                    self.array[i][j].boxColour = "44m" #set dark blue bg, white text
                    

                st=chr(ord(st[0])+1)
            num=num-1
        self.placeChessPieces()
        CHESSBOARD=self.array

    def placeChessPieces(self):
        
        st="a"
        for it in range(8):         #Placing Black Pawns
            
            st+=str(7)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chesspiece=Pawn("black",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st="a"
        for it in range(8):         #Placing white Pawns           
            st+=str(2)   
            for rows in range(8):
                for cols in range(8):
                    if self.array[rows][cols].identifier==st:
                        row,column=rows,cols
                        self.array[row][column].chesspiece=Pawn("white",st)
                        break
                       
                      
            
            st=chr(ord(st[0])+1)

        st=ord('c')-ord('a')                     #Placing black Bishop(c8,f8)         
        self.array[0][st].chesspiece=Bishop("black","c8")
        st=ord('f')-ord('a')                               
        self.array[0][st].chesspiece=Bishop("black","f8")
       

        st=ord('c')-ord('a')                     #Placing white Bishop(c1,f1)            
        self.array[7][st].chesspiece=Bishop("white","c1")
        st=ord('f')-ord('a')                            
        self.array[7][st].chesspiece=Bishop("white","f1")              
                      

        st=0                    #Placing black Rook(a8,h8)         
        self.array[0][st].chesspiece=Rook("black","a8")
        st=ord('h')-ord('a')                                
        self.array[0][st].chesspiece=Rook("black","h8")
       

        st=0                    #Placing white Rook(a1,h1)            
        self.array[7][st].chesspiece=Rook("white","a1")
        st=ord('h')-ord('a')                            
        self.array[7][st].chesspiece=Rook("white","h1")     

        st=ord('b')-ord('a')                    #Placing black Knight(b8,g8)         
        self.array[0][st].chesspiece=Knight("black","b8")
        st=ord('g')-ord('a')                                
        self.array[0][st].chesspiece=Knight("black","g8")

        st=ord('b')-ord('a')                    #Placing White Knight(b8,g8)         
        self.array[7][st].chesspiece=Knight("white","b1")
        st=ord('g')-ord('a')                                
        self.array[7][st].chesspiece=Knight("white","g1")


        st=ord('d')-ord('a')                    #Placing black Queeen(d8)         
        self.array[0][st].chesspiece=Queen("black","d8")

        st=ord('e')-ord('a')                    #Placing black King(e8)         
        self.array[0][st].chesspiece=King("black","e8")


        st=ord('d')-ord('a')                    #Placing white Queeen(d1)         
        self.array[7][st].chesspiece=Queen("white","d1")

        st=ord('e')-ord('a')                    #Placing white King(e1)         
        self.array[7][st].chesspiece=King("white","e1")
        
        
    def moveChessPiece(self, current, destination, agent):
        st=ord(current[0])-ord('a')
        row=8-int(current[1])
        dst=ord(destination[0])-ord('a')
        drow=8-int(destination[1])
        valid=self.array[row][st].chesspiece.checkValidMove(current,destination)
        if valid==False:
            print("Invalid Move!")
            return 

        elif self.array[drow][dst].state==False:
            if self.array[drow][dst].chesspiece.colour==agent.colour:
                print("Invalid Move!")
                return 

        if self.array[row][st].chesspiece.pathClear(current,destination,self.array, agent)==False:
            return

    

        if self.array[drow][dst].state==False:
            if self.array[drow][dst].chesspiece.colour!=agent.colour:
                agent.attacked+=1
                agent.attackedPieces.append(self.array[drow][dst].chesspiece)
                self.array[drow][dst].chesspiece.remove()

        self.array[drow][dst].chesspiece=copy.deepcopy(self.array[row][st].chesspiece)
        self.array[drow][dst].state=False
        self.array[row][st].chesspiece.remove()
        self.array[row][st].state=True
        print(self.array[row][st].identifier+" is emptied!")

    def countPieces(self, pieceName, colour):
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

        return material

    def positionsFunction(self):
        evaluation=0
        for i in range(8):
            for j in range(8):
                if (self.array[i][j].state==False):
                    if (self.array[i][j].chessPiece.identifier='p'):
                        evaluation+=pawnTable[i][j]
                    if (self.array[i][j].chessPiece.identifier='k'):
                        evaluation+=knightTable[i][j]
                    if (self.array[i][j].chessPiece.identifier='b'):
                        evaluation+=bishopTable[i][j]
                    if (self.array[i][j].chessPiece.identifier='r'):
                        evaluation+=rookTable[i][j]
                    if (self.array[i][j].chessPiece.identifier='Q'):
                        evaluation+=queenTable[i][j]

        return evaluation

    def evaluationFunction(self):
        m=self.materialFunction()
        e=self.positionsFunction()
        #chesspieces positions evaluation
        return m+e
        

    def displayChessBoard(self):
        for i in range(8):
            for j in range(8):
                if self.array[i][j].state==True:
                    print("\033["+self.array[i][j].textStyle+";"+self.array[i][j].textColour+";"+self.array[i][j].boxColour, self.array[i][j].identifier, end=" ")
                else:
                    print("\033["+self.array[i][j].textStyle+";"+self.array[i][j].chesspiece.colourID+";"+self.array[i][j].boxColour, self.array[i][j].chesspiece.name+" ", end=" ")
                    #print(self.array[i][j].boxColour, self.array[i][j].chesspiece.name+" ", end=" ")
            print("")
    def updateChessBoard():
        pass

class chessPiece:

    def __init__(self, name, colour, position):
        self.name=name
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
        self.colour="null"

class Pawn(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♟',colour,position)
        self.move=0 #Can take two steps in first move

    def checkValidMove(self,currentpos, destpos):
        #Pawn can move only forward and diagonally(if opponent gets attacked)
        destxindex=int(destpos[1])
        destyindex=ord(destpos[0])
        if(ord(currentpos[0])+1==ord(destpos[0])):       #right diagonal
            if(int(currentpos[1])+1==int(destpos[1])):   
                    return True 
    
        if(ord(currentpos[0])-1==ord(destpos[0])):       #left diagonal
            if(int(currentpos[1])+1==int(destpos[1])):
                    return True 
        
        if(ord(currentpos[0])==ord(destpos[0])): #forward
            if(int(currentpos[1])+1==int(destpos[1])):
                    return True 
        

        return False    #Invalid Move

        
    
    def pathClear(self, currentpos, destpos, board, agent):
        pass


class Bishop(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♝',colour,position)

    def checkValidMove(self,currentpos, destpos):
        #Bishop can move diagonally 
 
        if(abs(ord(currentpos[0])-ord(destpos[0])) == abs(int(currentpos[1])-int(destpos[1]))):                    
            return True
        

        return False

    def pathClear(self, currentpos, destpos, board, agent):
        currxindex=int(currentpos[1])
        curryindex=ord(currentpos[0])-ord('a')
        destxindex=int(destpos[1])
        destyindex=ord(destpos[0])-ord('a')

        if(destxindex>currxindex and destyindex>curryindex):  #upper right diagonal
            currxindex+=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                curryindex+=1


        if(destxindex<currxindex and destyindex>curryindex):  #lower right diagonal
            currxindex-=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1
                curryindex+=1



        if(destxindex>currxindex and destyindex<curryindex):  #upper left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                curryindex-=1


        if(destxindex<currxindex and destyindex<curryindex):  #lower left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1
                curryindex-=1
                
        return True       


class Rook(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♜',colour,position)

    def checkValidMove(self,currentpos, destpos):

        if(ord(currentpos[0])==ord(destpos[0])):      
            return True
        if(int(currentpos[1])==int(destpos[1])):                
            return True
    
        return False


    def pathClear(self, currentpos, destpos, board, agent):
        currxindex=int(currentpos[1])
        curryindex=ord(currentpos[0])-ord('a')
        destxindex=int(destpos[1])
        destyindex=ord(destpos[0])-ord('a')

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex<destxindex ): #forward
            currxindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print(currxindex,curryindex, board[8-currxindex][curryindex].state)
                    print(destxindex,destyindex, board[8-destxindex][destyindex].state)
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex>destxindex ): #backward
            currxindex-=1 
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1


        if(curryindex<destyindex and currxindex==destxindex ): #right
            curryindex+=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move!")
                    return False
                curryindex+=1

        if(ord(currentpos[0])>ord(destpos[0]) and currxindex==destxindex ): #left
            curryindex-=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move1!")
                    return False
                curryindex-=1

        return True
          

class Knight(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♞',colour,position)

    def checkValidMove(self,currentpos, destpos):

        if(ord(currentpos[0])+1==ord(destpos[0])):       
            if(int(currentpos[1])+2==int(destpos[1]) or int(currentpos[1])-2==int(destpos[1]) ):                
                return True 
    
        if(ord(currentpos[0])-1==ord(destpos[0])):       
            if(int(currentpos[1])+2==int(destpos[1]) or int(currentpos[1])-2==int(destpos[1]) ):                
                return True  
    
        return False    #Invalid Move
    
    def pathClear(self, currentpos, destpos, board, agent):
        pass


class Queen(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♛',colour,position)

    def checkValidMove(self,currentpos, destpos):

        if(ord(currentpos[0])==ord(destpos[0])):      
            return True
        if(int(currentpos[1])==int(destpos[1])):                
            return True
        if(abs(ord(currentpos[0])-ord(destpos[0])) == abs(int(currentpos[1])-int(destpos[1]))):                    
            return True


        return False

    def pathClear(self, currentpos, destpos, board, agent):
        currxindex=int(currentpos[1])
        curryindex=ord(currentpos[0])-ord('a')
        destxindex=int(destpos[1])
        destyindex=ord(destpos[0])-ord('a')

        

        if(destxindex>currxindex and destyindex>curryindex):  #upper right diagonal
            currxindex+=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move1!")
                    return False
                currxindex+=1
                curryindex+=1
            return True

        if(destxindex<currxindex and destyindex>curryindex):  #lower right diagonal
            currxindex-=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move2!")
                    return False
                currxindex-=1
                curryindex+=1
            return True


        if(destxindex>currxindex and destyindex<curryindex):  #upper left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move3!")
                    return False
                currxindex+=1
                curryindex-=1
            return True

        if(destxindex<currxindex and destyindex<curryindex):  #lower left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move4!")
                    return False
                currxindex-=1
                curryindex-=1
            return True

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex<destxindex ): #forward
            currxindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print(currxindex,curryindex, board[8-currxindex][curryindex].state)
                    print(destxindex,destyindex, board[8-destxindex][destyindex].state)
                    print("Path not clear/Invalid move5!")
                    return False
                currxindex+=1
            return True   

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex>destxindex ): #backward
            currxindex-=1 
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move6!")
                    return False
                currxindex-=1
            return True

        if(curryindex<destyindex and currxindex==destxindex ): #right
            curryindex+=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move7!")
                    return False
                curryindex+=1
            return True

        if(ord(currentpos[0])>ord(destpos[0]) and currxindex==destxindex ): #left
            curryindex-=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].state==False):
                    print("Path not clear/Invalid move8!")
                    return False
                curryindex-=1
            return True

        return True
                
    
class King(chessPiece):
    def __init__(self, colour, position):
        chessPiece.__init__(self,'♚',colour,position)

    def checkValidMove(self,currentpos,destpos):
        if(ord(currentpos[0])+1==ord(destpos[0])):       #right diagonal
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
                return True
            
            
        return False    #Invalid Move

    def pathClear(self, currentpos, destpos, board, agent):
        pass



class Agent:
    def __init__(self, turn, colour):
        self.turn=turn #A flag that is true when its Computer's turn
        self.colour=colour
        self.attacked=0        
        self.attackedPieces=[]



board=chessBoard()
board.initializeBoard()
board.displayChessBoard()

user=Agent(True, "White")  #We will have two agents, user and chess bot
chessBot=Agent(False, "Black")

while(1):
    print("\033[1;32;40m Enter current position and destined position\n")
    currentpos=input()
    destpos=input()
    board.moveChessPiece(currentpos,destpos, user)
    board.displayChessBoard()

#1. prompt user to enter his move (store moves as well)
#2. update chessboard
#3. Agent's turn (decide which move is the best using minmax and alpha puning)
#4. update chessboard
#5. display it
#6. repeat