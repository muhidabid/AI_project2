# GIVEN A BOARD AND A COLOUR, THESE FUNCTIONS GENERATE MOVES AND RETURN THEM AS LIST

class Move:
    def __init__(self, startX, startY, endX, endY):
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

def generatePawnMoves(colour, board):
    moves = []

    if colour == 'white':
        for i in range(8):
            for j in range(8):
                if board[i][j].chessPiece.name == 'pawn' and board[i][j].chessPiece.colour == 'white':
                    if i==6:
                        if board[i][j].chessPiece.checkValidMove(i, j, i-1, j, board, colour): moves.append(Move(i, j, i-1, j))
                        if board[i][j].chessPiece.checkValidMove(i, j, i-2, j, board, colour): moves.append(Move(i, j, i-2, j))                        
                    elif i-1>=0 and board[i][j].chessPiece.checkValidMove(i, j, i-1, j, board, colour): moves.append(Move(i, j, i-1, j))
    elif colour == 'black':
        for i in range(8):
            for j in range(8):
                if board[i][j].chessPiece.name == 'pawn' and board[i][j].chessPiece.colour == 'black':
                    if i==1:
                        if board[i][j].chessPiece.checkValidMove(i, j, i+1, j, board, colour): moves.append(Move(i, j, i+1, j))
                        if board[i][j].chessPiece.checkValidMove(i, j, i+2, j, board, colour): moves.append(Move(i, j, i+2, j))                        
                    elif i+1<=7 and board[i][j].chessPiece.checkValidMove(i, j, i+1, j, board, colour): moves.append(Move(i, j, i+1, j))

    return moves

def generateBishopMoves(colour, board):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j].chessPiece.name == 'bishop' and board[i][j].chessPiece.colour == colour:
                # top right diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    tempY = tempY+1
                    if tempX < 0 or tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # top left diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    tempY = tempY-1
                    if tempX < 0 or tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # bottom right diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    tempY = tempY+1
                    if tempX > 7 or tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # bottom left diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    tempY = tempY-1
                    if tempX > 7 or tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
    return moves
    
def generateRookMoves(colour, board):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j].chessPiece.name == 'rook' and board[i][j].chessPiece.colour == colour:
                #up
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    if tempX < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #down
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    if tempX > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #right
                tempX = i
                tempY = j
                while 1:
                    tempY = tempY+1
                    if tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #left
                tempX = i
                tempY = j
                while 1:
                    tempY = tempY-1
                    if tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
    return moves

def generateKnightMoves(colour, board):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j].chessPiece.name == 'knight' and board[i][j].chessPiece.colour == colour:
                # if conditions going clockwise starting top right
                # right half of moves
                if i-2 >= 0 and j+1 <= 7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-2, j+1, board, colour):moves.append(Move(i,j,i-2,j+1))
                if i-1 >= 0 and j+2 <= 7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-1, j+2, board, colour):moves.append(Move(i,j,i-1,j+2))
                if i+1 <= 7 and j+2 <= 7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+1, j+2, board, colour):moves.append(Move(i,j,i+1,j+2))
                if i+2 <= 7 and j+1 <= 7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+2, j+1, board, colour):moves.append(Move(i,j,i+2,j+1))
                # left half of moves
                if i+2 <= 7 and j-1 >= 0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+2, j-1, board, colour):moves.append(Move(i,j,i+2,j-1))
                if i+1 <= 7 and j-2 >= 0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+1, j-2, board, colour):moves.append(Move(i,j,i+1,j-2))
                if i-1 >= 0 and j-2 >= 0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-1, j-2, board, colour):moves.append(Move(i,j,i-1,j-2))
                if i-2 >= 0 and j-1 >= 0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-2, j-1, board, colour):moves.append(Move(i,j,i-2,j-1))
    return moves

def generateKingMoves(colour, board):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j].chessPiece.name == 'king' and board[i][j].chessPiece.colour == colour:
                # moving clockwise starting top left
                if i-1>=0 and j-1>=0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-1, j-1, board, colour):moves.append(Move(i,j,i-1,j-1))
                if i-1>=0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-1, j, board, colour):moves.append(Move(i,j,i-1,j))
                if i-1>=0 and j+1<=7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i-1, j+1, board, colour):moves.append(Move(i,j,i-1,j+1))
                if j+1<=7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i, j+1, board, colour):moves.append(Move(i,j,i,j+1))
                if i+1<=7 and j+1<=7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+1, j+1, board, colour):moves.append(Move(i,j,i+1,j+1))
                if i+1<=7:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+1, j, board, colour):moves.append(Move(i,j,i+1,j))
                if i+1<=7 and j-1>=0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i+1, j-1, board, colour):moves.append(Move(i,j,i+1,j-1))
                if j-1>=0:
                    if board[i][j].chessPiece.checkValidMove(i, j, i, j-1, board, colour):moves.append(Move(i,j,i,j-1))
    return moves

def generateQueenMoves(colour, board):
    moves = []
    for i in range(8):
        for j in range(8):
            if board[i][j].chessPiece.name == 'queen' and board[i][j].chessPiece.colour == colour:
                # ROOK MOVES
                #up
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    if tempX < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #down
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    if tempX > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #right
                tempX = i
                tempY = j
                while 1:
                    tempY = tempY+1
                    if tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                #left
                tempX = i
                tempY = j
                while 1:
                    tempY = tempY-1
                    if tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i,j,tempX,tempY))
                # BISHOP MOVES
                # top right diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    tempY = tempY+1
                    if tempX < 0 or tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # top left diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX-1
                    tempY = tempY-1
                    if tempX < 0 or tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # bottom right diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    tempY = tempY+1
                    if tempX > 7 or tempY > 7:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
                # bottom left diagonal moves
                tempX = i
                tempY = j
                while 1:
                    tempX = tempX+1
                    tempY = tempY-1
                    if tempX > 7 or tempY < 0:
                        break
                    elif board[i][j].chessPiece.checkValidMove(i, j, tempX, tempY, board, colour):
                        moves.append(Move(i, j, tempX, tempY))
    return moves

