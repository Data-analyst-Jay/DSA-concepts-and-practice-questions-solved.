#TC = O(9^empty cells) SC = O(1)

def is_safe(board,row,col,dig):
    for i in range(9):
        if board[row][i] == dig:
            return False
        if board[i][col] == dig:
            return False
    
    sr, sc = (row//3)*3, (col//3)*3
    for i in range(sr,sr+3):
        for j in range(sc,sc+3):
            if board[i][j] == dig:
                return False
    return True

def h2(board,row,col):
    if row == 9:
        return True
    next_r = row
    next_c = col+1
    if col == 8:
        next_r = row+1
        next_c = 0
    if board[row][col] != '.':
        return h2(board,next_r,next_c)
    
    for i in range(1,10):
        if is_safe(board,row,col,str(i)):
            board[row][col] = str(i)
            if h2(board,next_r,next_c):
                return True
            board[row][col] = '.'
    return False

def SolveSudoku(board):
    if h2(board,0,0):
        return board
    return False

arr = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans = SolveSudoku(arr)
print(ans)