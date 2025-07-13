#LC 1008
#TC = O(n) but brute force is o(n^2)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder):
       i = 0
       return self.helper(preorder, i, int('inf'))
    def helper(self, preorder, i, bound):
        if i >= len(preorder) or preorder[i] > bound:
            return None
        root = TreeNode(preorder[0])
        i+=1
        root.left = self.helper(preorder, i, root.val)
        root.right = self.helper(preorder, i, bound)
        return root
