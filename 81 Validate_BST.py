class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, min, max):
        if root == None:
            return True
        if min is not None and root.val <= min:
            return False
        if max is not None and root.val >= max:
            return False
        return (self.helper(root.left, min , root.val) and self.helper(root.right, root.val, max))
    def isValidBST(self, root):
        return self.helper(root, None, None)