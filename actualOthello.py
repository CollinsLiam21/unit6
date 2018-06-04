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
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*c,A*r))
            if data['board'][r][c] == 1:
                Sprite(whiteCircle,(A*c,A*r))
                i += 1
            elif data['board'][r][c] == 2:
                Sprite(blackCircle,(A*c,A*r))
                i += 1
    if winner() == True and boardFull() == True:
        Sprite(winBlack, (500,150))
    elif winner() == False and boardFull() == True:
        Sprite(winWhite, (500,250))

def winner():
    blackTotal = 0
    whiteTotal = 0
    for r in range(0,8):
        for c in range(0,8):
            if data['board'][r][c] == 1:
                whiteTotal += 1
            elif data['board'][r][c] == 2:
                blackTotal += 1
    if blackTotal > whiteTotal:
        return True
    elif whiteTotal > blackTotal:
        return False

def boardFull():
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            if data['board'][r][c] == 1:
                i += 1
            elif data['board'][r][c] == 2:
                i += 1
    if i == 64:
        return True
    else:
        return False
                
def flipPieces(rowLast,colLast):
    if colLast != 7 and data['board'][rowLast][colLast + 1] != 0:
        flipEast(rowLast,colLast)
    if colLast != 0 and data['board'][rowLast][colLast - 1] != 0:
        flipWest(rowLast,colLast)
    if rowLast != 0 and data['board'][rowLast - 1][colLast] != 0:
        flipNorth(rowLast,colLast)
    if rowLast != 7 and data['board'][rowLast + 1][colLast] != 0:
        flipSouth(rowLast,colLast)
    if colLast != 0 and rowLast != 0 and data['board'][rowLast - 1][colLast - 1] != 0:
        flipNorthWest(rowLast,colLast)
    if colLast != 7 and rowLast != 0 and data['board'][rowLast - 1][colLast + 1] != 0:
        flipNorthEast(rowLast,colLast)
    if colLast != 0 and rowLast != 7 and data['board'][rowLast + 1][colLast - 1] != 0:
        flipSouthWest(rowLast,colLast)
    if colLast != 7 and rowLast != 7 and data['board'][rowLast + 1][colLast + 1] != 0:
        flipSouthEast(rowLast,colLast)
    redrawAll()


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
    winBlack = TextAsset('Black Has Won the Game!',fill=green,style='bold 30pt Times')
    winWhite = TextAsset('White Has Won the Game!',fill=green,style='bold 30pt Times')
    Tie = TextAsset('We Have A Tie!',fill=green,style='bold 30pt Times')
    
    redrawAll()
    
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
