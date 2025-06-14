class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def kthSmallest(self, root, k):
        if root == None:
            return -1
        
        if root.left:
            lans = self.kthSmallest(root.left, k)
            if lans != -1:
                return lans
        
        if self.count + 1 == k:
            return root.val
        self.count += 1

        if root.right:
            rans = self.kthSmallest(root.right, k)
            if rans != -1:
                return rans
        
        return -1