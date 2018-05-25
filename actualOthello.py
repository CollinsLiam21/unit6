#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *

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
    
    white = Color(0x000000,1)
    black = Color(0xFFFFFF,1)
    green = Color(0x00FF00,1)
    
    greenGrid = RectangleAsset(500,500,LineStyle(1,black),green)
    Sprite(greenGrid)
    
    #App().listenMouseEvent('click',mouseClick)
    App().run()
