# LC105

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self,inorder,preorder,pindx,left,right):
        if left > right:
            return None
        root = TreeNode(preorder[pindx])
        i = inorder.index(preorder[pindx])
        root.left = self.helper(inorder,preorder,pindx+1,left,i-1)
        root.right = self.helper(inorder,preorder,pindx+i-left+1,i+1,right)
        return root


    def buildTree(self, preorder, inorder):
        pindx = 0
        ans = self.helper(inorder,preorder,pindx,0,len(inorder)-1)
        return ans