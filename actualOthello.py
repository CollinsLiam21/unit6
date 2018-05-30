#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *

A = 60

def buildBoard():
    board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    board[4][4] = 2
    board[3][3] = 2
    board[3][4] = 1
    board[4][3] = 1
    return board

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    A = 60
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*r,A*c))
            if data['board'][r][c] == 1:
                Sprite(whiteCircle,(A*r,A*c))
            elif data['board'][r][c] == 2:
                Sprite(blackCircle,(A*r,A*c))
                
def flipPieces(rowLast,colLast):
    flipEast(rowLast,colLast)

def flipEast(rowLast,colLast):
    if data['board'][rowLast][colLast] == 1 and data['board'][rowLast][colLast+2] == 1 and data['board'][rowLast][colLast+1] == 2:
        data['board'][rowLast][colLast+1] = 1
        redrawAll()
    
            

def mouseClick(event):
    column = int(event.x//A)
    row = int(event.y//A)
    if data['turn'] == 1:
        data['board'][column][row] = 1
        data['turn'] = 2
        redrawAll()
        flipPieces(row,column)
    else:
        data['board'][column][row] = 2
        data['turn'] = 1
        redrawAll()
        flipPieces(row,column)
    
    

if __name__ == '__main__':
    
    
    data = {}
    data['board'] = buildBoard()
    data['turn'] = 1
    
    whiteCircle = CircleAsset(A/2,LineStyle(1,white),white)
    blackCircle = CircleAsset(A/2,LineStyle(1,black),black)
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    redrawAll()
    
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
