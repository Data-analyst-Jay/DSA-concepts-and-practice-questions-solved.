# TC = o(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        q = []
        q.append((root,0))
        maxwidth = 0
        while q:
            st = q[0][1]
            end = q[-1][1]
            maxwidth = max(maxwidth, end - st + 1)
            for i in range(len(q)):
                node, idx = q.pop(0)
                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))
        return maxwidth