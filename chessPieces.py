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
        
class Pawn(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'pawn','♟',colour,position,10)
        elif colour == "black":
            chessPiece.__init__(self,'pawn','♟',colour,position,-10)
         """
        chessPiece.__init__(self,'pawn','♟',colour,position,10)
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
        """ if colour == "white":
            chessPiece.__init__(self,'bishop','♝',colour,position,30)
        elif colour == "black":
            chessPiece.__init__(self,'bishop','♝',colour,position,-30) """
        chessPiece.__init__(self,'bishop','♝',colour,position,30)
        

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
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                curryindex+=1


        if(destxindex<currxindex and destyindex>curryindex):  #lower right diagonal
            currxindex-=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1
                curryindex+=1



        if(destxindex>currxindex and destyindex<curryindex):  #upper left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                curryindex-=1


        if(destxindex<currxindex and destyindex<curryindex):  #lower left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1
                curryindex-=1
                
        return True       

class Rook(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'rook','♜',colour,position,50)
        elif colour == "black":
            chessPiece.__init__(self,'rook','♜',colour,position,-50)"""
        chessPiece.__init__(self,'rook','♜',colour,position,50)

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
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print(currxindex,curryindex, board[8-currxindex][curryindex].isEmpty)
                    print(destxindex,destyindex, board[8-destxindex][destyindex].isEmpty)
                    print("Path not clear/Invalid move!")
                    return False
                currxindex+=1
                

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex>destxindex ): #backward
            currxindex-=1 
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                currxindex-=1


        if(curryindex<destyindex and currxindex==destxindex ): #right
            curryindex+=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move!")
                    return False
                curryindex+=1

        if(ord(currentpos[0])>ord(destpos[0]) and currxindex==destxindex ): #left
            curryindex-=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move1!")
                    return False
                curryindex-=1

        return True
          
class Knight(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'knight','♞',colour,position,30)
        elif colour == "black":
            chessPiece.__init__(self,'knight','♞',colour,position,-30)"""
        chessPiece.__init__(self,'knight','♞',colour,position,30)
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
        """ if colour == "white":
            chessPiece.__init__(self,'queen','♛',colour,position,90)
        elif colour == "black":
            chessPiece.__init__(self,'queen','♛',colour,position,-90) """
        chessPiece.__init__(self,'queen','♛',colour,position,90)

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
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move1!")
                    return False
                currxindex+=1
                curryindex+=1
            return True

        if(destxindex<currxindex and destyindex>curryindex):  #lower right diagonal
            currxindex-=1
            curryindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move2!")
                    return False
                currxindex-=1
                curryindex+=1
            return True


        if(destxindex>currxindex and destyindex<curryindex):  #upper left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move3!")
                    return False
                currxindex+=1
                curryindex-=1
            return True

        if(destxindex<currxindex and destyindex<curryindex):  #lower left diagonal
            currxindex+=1
            curryindex-=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move4!")
                    return False
                currxindex-=1
                curryindex-=1
            return True

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex<destxindex ): #forward
            currxindex+=1
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print(currxindex,curryindex, board[8-currxindex][curryindex].isEmpty)
                    print(destxindex,destyindex, board[8-destxindex][destyindex].isEmpty)
                    print("Path not clear/Invalid move5!")
                    return False
                currxindex+=1
            return True   

        if(ord(currentpos[0])==ord(destpos[0]) and currxindex>destxindex ): #backward
            currxindex-=1 
            while(currxindex!=destxindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move6!")
                    return False
                currxindex-=1
            return True

        if(curryindex<destyindex and currxindex==destxindex ): #right
            curryindex+=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move7!")
                    return False
                curryindex+=1
            return True

        if(ord(currentpos[0])>ord(destpos[0]) and currxindex==destxindex ): #left
            curryindex-=1
            while(curryindex!=destyindex):
                if(board[8-currxindex][curryindex].isEmpty==False):
                    print("Path not clear/Invalid move8!")
                    return False
                curryindex-=1
            return True

        return True
                
class King(chessPiece):
    def __init__(self, colour, position):
        """ if colour == "white":
            chessPiece.__init__(self,'king','♚',colour,position,900)
        elif colour == "black":
            chessPiece.__init__(self,'king','♚',colour,position,-900) """
        chessPiece.__init__(self,'king','♚',colour,position,900)

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