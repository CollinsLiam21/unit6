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
    A = 60
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    blackLine = LineAsset(0,A,LineStyle(4,black))
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*r,A*c))
            if data['board'][r][c] == 1:
                Sprite(whiteCircle,(A*r,A*c))
            if data['board'][r][c] == 2:
                Sprite(blackCircle,(A*r,A*c))
            
            

def mouseClick(event):
    #board[row][column] = 1
    column = event.x//A
    row = event.y//A
    if data['board'].count(1) == data['board'].count(2):
        data['board'][row][column] = 1
    if data['board'].count(1) > data['board'].count(2):
        data['board'][row][column] = 2
    

if __name__ == '__main__':
    
    
    data = {}
    data['board'] = buildBoard()
    
    whiteCircle = CircleAsset(A/2,LineStyle(1,white),white)
    blackCircle = CircleAsset(A/2,LineStyle(1,black),black)
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    redrawAll()
    
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
