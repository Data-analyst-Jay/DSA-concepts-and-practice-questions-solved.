def LCA(root, p, q):
    if not root:
        return None
    if root == p or root == q:
        return root

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if left and right:
        return root
    return left if left else right