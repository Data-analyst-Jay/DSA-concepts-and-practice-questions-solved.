# TC = O(8^(n^2)) # n^2 is the size of the grid
# SC = O(n^2)
class Solution:
    def checkValidGrid(self, M):
        n = (len(M))
        ans = self.isvalid(M, 0, 0, n, 0)
        return ans 

    def isvalid(self, M, r, c, n, exp_val):
        if (r < 0 or c < 0 or r >= n or c >= n or M[r][c] != exp_val):
            return False
        if (exp_val == (n**2) - 1):
            return True
        ans1 = self.isvalid(M, r-2, c+1, n, exp_val+1)
        ans2 = self.isvalid(M, r-1, c+2, n, exp_val+1)
        ans3 = self.isvalid(M, r+1, c+2, n, exp_val+1)
        ans4 = self.isvalid(M, r+2, c+1, n, exp_val+1)
        ans5 = self.isvalid(M, r+2, c-1, n, exp_val+1)
        ans6 = self.isvalid(M, r+1, c-2, n, exp_val+1)
        ans7 = self.isvalid(M, r-1, c-2, n, exp_val+1)
        ans8 = self.isvalid(M, r-2, c-1, n, exp_val+1)

        return (ans1 or ans2 or ans3 or ans4 or ans5 or ans6 or ans7 or ans8)
    
grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
a = Solution()
print(a.checkValidGrid(grid)) # True