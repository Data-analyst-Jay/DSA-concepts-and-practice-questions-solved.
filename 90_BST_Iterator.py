#LC = 173
#TC = o(1) (Amortized or average) and SC = O(h) where h is the height of the tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        self.s = []
        self.helper(root)
        
    def helper(self, root):
        while root:
            self.s.append(root)
            root = root.left

    def next(self):
        self.ans = self.s.pop()
        if self.ans.right:
            self.helper(self.ans.right)
        return self.ans.val

    def hasNext(self):
        return len(self.s) > 0