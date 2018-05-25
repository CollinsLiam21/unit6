#Liam Collins
#5/23/18
#actualOthello.py

def buildBoard(board):
    for r in range(0,8):
        for c in range(0,8):
            print(board[r][c],end=' ')
        print()

board = [['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','',''],['x','','','','','','','']]
buildBoard(board)

row = int(input('Enter a row: '))
col = int(input('Enter a column: '))
board[row-1][col-1] = 'X'
buildBoard(board)
