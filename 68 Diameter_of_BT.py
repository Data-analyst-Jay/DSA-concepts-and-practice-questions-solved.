def height(self,root):
        if root == None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh,rh) +1

def diameter(self,root):                     #TC = O(n^2)
        if root == None:
            return 0
        ld = self.diameter(root.left)  
        rd = self.diameter(root.right)      
        nd = self.height(root.left) + self.height(root.right) + 1
        return max(ld,rd,nd)                  

class solution:
    def __init__(self):
            self.ans = 0

    def height(self,root):
        if root == None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.ans = max(self.ans,lh+rh+1)  
        return max(lh,rh) + 1
    
    def optimalDiameter(self,root):
          self.ans = 0
          self.height(root)
          return self.ans        