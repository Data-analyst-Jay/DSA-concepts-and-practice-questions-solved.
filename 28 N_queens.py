# TC = O(n!)
def issafe(board,row,col,n):           #TC = O(n)
    #Horizontal
    for j in range(col):
        if board[row][j] == 'Q':
            return False
    
    #Verticle
    for j in range(row):
        if board[j][col] == 'Q':
            return False
   
    #Left diagonal
    i,j = row, col
    while i>=0 and j>=0:
        if board[i][j] == 'Q':
            return False
        i-=1
        j-=1
    
    #Right diagonal
    i, j = row, col
    while i>=0 and j<n:
        if board[i][j] == 'Q':
            return False
        i-=1
        j+=1
   
    return True

def nqueens(board,row,n,ans):              #TC = O(n!)
    if row == n:
        ans.append([''.join(r) for r in board])
        return
    for col in range(n):
        if issafe(board,row,col,n):
            board[row][col] = 'Q'
            nqueens(board,row+1,n,ans)
            board[row][col] = '.'

def solveNQueens(n):
    board = [['.' for i in range(n)] for j in range(n)]
    ans = []
    nqueens(board,0,n,ans)
    return ans

ans = solveNQueens(4)
print(ans)