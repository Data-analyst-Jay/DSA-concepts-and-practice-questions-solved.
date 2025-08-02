#Tc = o(n) SC = o(height of the tree)

def sumtree(root):
    if root is None:
        return 0
    ls = sumtree(root.left)
    rs = sumtree(root.right)
    root.val += ls + rs
    return root.val
