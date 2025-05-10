# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allpaths(self, root, path, ans):
        if root.left is None and root.right is None:
            ans.append(path)
            return
        path += "->"
        if root.left:
            self.allpaths(root.left, path + str(root.left.val), ans)
        if root.right:
            self.allpaths(root.right, path + str(root.right.val), ans)

    def binaryTreePaths(self, root):
        ans = []
        path = str(root.val)
        self.allpaths(root, path, ans)
        return ans
    
