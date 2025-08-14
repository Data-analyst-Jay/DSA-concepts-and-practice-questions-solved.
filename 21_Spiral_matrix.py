L = [[1,2,3],[4,5,6],[7,8,9]]
# O(m*n)
def spiral(M):
    s_row, e_row, s_col, e_col = 0, len(M)-1, 0, len(M[0])-1
    ans = []
    while s_row <= e_row and s_col <= e_col:
        for i in range(s_col, e_col+1):         # Top
            ans.append(M[s_row][i],)
        for i in range(s_row+1, e_row+1):       # Right
            ans.append(M[i][e_col],)
        for i in range(e_col-1, s_col, -1):     # Bottom
            if s_row == e_row:
                break
            ans.append(M[e_row][i],)
        for i in range(e_row, s_row, -1):       # Left
            if s_col == e_col:
                break
            ans.append(M[i][s_col],)
        s_row +=1
        e_row -= 1
        s_col += 1
        e_col -= 1 
    print(ans)

spiral(L)