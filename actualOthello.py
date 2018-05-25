#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *

A = 500

def buildBoard(board):
    for r in range(0,8):
        for c in range(0,8):
            print(board[r][c],end=' ')
        print()

board = [['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','','']]
#buildBoard(board)

'''row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
buildBoard(board)'''

if __name__ == '__main__':
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    blackLine = LineAsset(0,A,LineStyle(4,black)) #x_endpoint, y_endpoint, lineStyle
    
    
    Sprite(greenGrid)
    Sprite(blackLine, (A/8,0))
    Sprite(blackLine, ((A/8)*2,0))
    Sprite(blackLine, ((A/8)*3,0))
    Sprite(blackLine, ((A/8)*4,0))
    Sprite(blackLine, ((A/8)*5,0))
    Sprite(blackLine, ((A/8)*6,0))
    Sprite(blackLine, ((A/8)*7,0))
    
    
    #App().listenMouseEvent('click',mouseClick)
    App().run()
