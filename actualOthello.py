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
            Sprite(greenGrid,(A*c,A*r))
            if data['board'][r][c] == 1:
                Sprite(whiteCircle,(A*c,A*r))
            elif data['board'][r][c] == 2:
                Sprite(blackCircle,(A*c,A*r))
                
def flipPieces(rowLast,colLast):
    if colLast != 7:
        flipEast(rowLast,colLast)
    if colLast != 0:
        flipWest(rowLast,colLast)
    flipNorth(rowLast,colLast)
    flipSouth(rowLast,colLast)
    flipNorthWest(rowLast,colLast)
    flipNorthEast(rowLast,colLast)
    flipSouthWest(rowLast,colLast)
    flipSouthEast(rowLast,colLast)


def flipEast(rowLast,colLast):
    i = 1
    while data['board'][rowLast][colLast + i] == data['turn']:
        i += 1
    if data['board'][rowLast][colLast + i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast][colLast + i -1] = 1
                i -= 1
            else:
                data['board'][rowLast][colLast + i -1] = 2
                i -= 1
    redrawAll()
    
def flipWest(rowLast,colLast):
    i = 1
    while data['board'][rowLast][colLast - i] == data['turn']:
        i += 1
    if data['board'][rowLast][colLast - i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast][colLast - i + 1] = 1
                i -= 1
            else:
                data['board'][rowLast][colLast - i + 1] = 2
                i -= 1
    redrawAll()

def flipNorth(rowLast,colLast):
    i = 1
    while data['board'][rowLast - i][colLast] == data['turn']:
        i += 1
    if data['board'][rowLast - i][colLast] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast - i +1][colLast] = 1
                i -= 1
            else:
                data['board'][rowLast - i +1][colLast] = 2
                i -= 1
    redrawAll()
    
def flipSouth(rowLast,colLast):
    i = 1
    while data['board'][rowLast + i][colLast] == data['turn']:
        i += 1
    if data['board'][rowLast + i][colLast] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast + i -1][colLast] = 1
                i -= 1
            else:
                data['board'][rowLast + i -1][colLast] = 2
                i -= 1
    redrawAll()
    
def flipNorthWest(rowLast,colLast):
    i = 1
    while data['board'][rowLast - i][colLast - i] == data['turn']:
        i += 1
    if data['board'][rowLast - i][colLast - i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast - i + 1][colLast - i + 1] = 1
                i -= 1
            else:
                data['board'][rowLast - i + 1][colLast - i + 1] = 2
                i -= 1
    redrawAll()
    
def flipNorthEast(rowLast,colLast):
    i = 1
    while data['board'][rowLast - i][colLast + i] == data['turn']:
        i += 1
    if data['board'][rowLast - i][colLast + i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast - i + 1][colLast + i - 1] = 1
                i -= 1
            else:
                data['board'][rowLast - i + 1][colLast + i - 1] = 2
                i -= 1
    redrawAll()
    
def flipSouthWest(rowLast,colLast):
    i = 1
    while data['board'][rowLast + i][colLast - i] == data['turn']:
        i += 1
    if data['board'][rowLast + i][colLast - i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast + i - 1][colLast - i + 1] = 1
                i -= 1
            else:
                data['board'][rowLast + i - 1][colLast - i + 1] = 2
                i -= 1
    redrawAll()
    
def flipSouthEast(rowLast,colLast):
    i = 1
    while data['board'][rowLast + i][colLast + i] == data['turn']:
        i += 1
    if data['board'][rowLast + i][colLast + i] !=0:
        print('flipping')
        while i > 1:
            if data['turn'] == 2:
                data['board'][rowLast + i - 1][colLast + i - 1] = 1
                i -= 1
            else:
                data['board'][rowLast + i - 1][colLast + i - 1] = 2
                i -= 1
    redrawAll()

def mouseClick(event):
    column = int(event.x//A)
    row = int(event.y//A)
    if data['turn'] == 1:
        data['board'][row][column] = 1
        data['turn'] = 2
        flipPieces(row,column)
    else:
        data['board'][row][column] = 2
        data['turn'] = 1
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
