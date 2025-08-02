# LC116 #TC O(n) #SC O(1)

# Definition for a Node.

class Node:
    def __init__(self, val, left, right, next:None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root or not root.left:
            return
        
        q = []
        q.append(root)
        q.append(None)
        temp, curr = None, None
        while q:
            curr = q.pop(0)
            if not curr:
                if not q:
                    break
                q.append(None)
            else:
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                if temp is not None:
                    temp.next = curr
            temp = curr
        return root