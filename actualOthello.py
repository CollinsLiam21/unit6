#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *



def buildBoard():
    board = [['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','',''],['','','','','','','','']]
    
def redrawall():
    A = 60
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    blackLine = LineAsset(0,A,LineStyle(4,black))
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*r,A*c))


#buildBoard(board)

'''row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
buildBoard(board)'''

if __name__ == '__main__':
    
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    redrawall()
    
    
    #App().listenMouseEvent('click',mouseClick)
    App().run()
