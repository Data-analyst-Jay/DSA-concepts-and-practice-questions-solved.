# TC = O(n)
# class TreeNode:
def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        ans = []
        curr = root
        while curr:
            if curr.left is None:
                  ans.append(curr.val)
                  curr = curr.right
            else:
                IP = curr.left
                while IP.right and IP.right != curr:
                      IP = IP.right
                
                if IP.right is None:
                    IP.right = curr
                    curr = curr.left

                else:
                    IP.rigtht = None
                    ans.append(curr.val)
                    curr = curr.right
        return ans