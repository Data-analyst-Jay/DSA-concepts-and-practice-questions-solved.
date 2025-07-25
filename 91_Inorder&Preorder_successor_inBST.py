# TC = O(h) SC = O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pred(root):
    root = root.left
    while root and root.right:
        root = root.right
    return root

def succ(root):
    root = root.right
    while root and root.left:
        root = root.left
    return root

def IPS(root, key):
    ip = [None, None]
    while root:
        if root.val > key:
            ip[1] = root
            root = root.left
        
        elif root.val < key:
            ip[0] = root
            root = root.right
        
        else:
            ip[0] = pred(root)
            ip[1] = succ(root)