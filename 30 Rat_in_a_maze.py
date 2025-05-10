class solution:
    def helper(self,M, r, c, n, ans, path):
        if r < 0 or c < 0 or r >= n or c >= n or M[r][c] == 0:
            return
        if r == n-1 and c == n-1:
            ans.append(path)
            return
        M[r][c] = 0
        self.helper(M, r+1, c, n, ans, path+'D')
        self.helper(M, r, c+1, n, ans, path+'R')
        self.helper(M, r-1, c, n, ans, path+'U')
        self.helper(M, r, c-1, n, ans, path+'L')
        M[r][c] = 1

    def findPath(self, M):
        n = len(M)
        ans = []
        path = ''
        self.helper(M, 0, 0, n, ans, path)
        return ans
    
A = solution()
a = A.findPath([[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0],[0,0,1,1,0],[0,0,0,1,1]])
print(a)