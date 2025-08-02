#TC = O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev = None
    def minDiffInBST(self, root):
        ans = float('inf')
        if not root:
            return float('inf')
        if root.left:
            leftmin = self.minDiffInBST(root.left)
            ans = min(ans, leftmin)
        if self.prev:
            ans = min(ans, root.val - self.prev)
        self.prev = root.val
        if root.right:
            rightmin = self.minDiffInBST(root.right)
            ans = min(ans, rightmin)
        return ans