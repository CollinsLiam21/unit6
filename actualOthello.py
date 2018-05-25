#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *



def buildBoard():
    board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    board[4][4] = 2
    board[3][3] = 2
    board[3][4] = 1
    board[4][3] = 1

def redrawAll():
    A = 60
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    blackLine = LineAsset(0,A,LineStyle(4,black))
    whiteCircle = CircleAsset(A-2,LineStyle(1,white),white)
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*r,A*c))
            
def mouseClick(event):
    


if __name__ == '__main__':
    
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    redrawAll()
    
    
    App().listenMouseEvent('click',mouseClick)
    App().run()
