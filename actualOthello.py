#Liam Collins
#5/23/18
#actualOthello.py

from ggame import *



def buildBoard():
    board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

def redrawAll():
    A = 60
    greenGrid = RectangleAsset(A,A,LineStyle(4,black),green)
    blackLine = LineAsset(0,A,LineStyle(4,black))
    whiteCircle = CircleAsset(A-2,
    for r in range(0,8):
        for c in range(0,8):
            Sprite(greenGrid,(A*r,A*c))
            
def mouseClick(event):
    if data['gameOver'] == False:
        if (event.x < A and event.y < A) and board[0][0] == 0:
            Sprite(x, (25,10))
            data['square1'] = 'x'
        elif (150 < event.x < 350 and event.y < 150) and isEmpty(2) == True:
            Sprite(x, (215,10))
            data['square2'] = 'x'
        elif (350 < event.x < 550 and event.y < 150) and isEmpty(3) == True:
            Sprite(x, (400,10))
            data['square3'] = 'x'
        elif (event.x < 150 and 150 < event.y < 350) and isEmpty(4) == True:
            Sprite(x, (25,180))
            data['square4'] = 'x'
        elif (150 < event.x < 350 and 150 < event.y < 350) and isEmpty(5) == True:
            Sprite(x, (215,180))
            data['square5'] = 'x'
        elif (350 < event.x < 550 and 150 < event.y < 350) and isEmpty(6) == True:
            Sprite(x, (400,180))
            data['square6'] = 'x'
        elif (event.x < 150 and 350 < event.y < 550) and isEmpty(7) == True:
            Sprite(x, (25,380))
            data['square7'] = 'x'
        elif (150 < event.x < 350 and 350 < event.y < 550) and isEmpty(8) == True:
            Sprite(x, (215,380))
            data['square8'] = 'x'
        elif (350 < event.x < 550 and 350 < event.y < 550) and isEmpty(9) == True:
            Sprite(x, (400,380))
            data['square9'] = 'x'


#buildBoard(board)

'''row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
buildBoard(board)'''

if __name__ == '__main__':
    
    
    white = Color(0xFFFFFF,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    
    redrawAll()
    
    
    #App().listenMouseEvent('click',mouseClick)
    App().run()
