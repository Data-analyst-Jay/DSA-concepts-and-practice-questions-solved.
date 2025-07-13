# LC = 99
# TC = O(n)

prev, first, second = None, None, None
def iot(root):
        if root == None:
            return
        iot(root.left)
        if prev != None and root.val < prev.val:
            if not first:
                first = prev
            second = root
        prev = root
        iot(root.right)

def recover_bst(root):
     iot(root)
     temp = first.val
     first.val = second.val
     second.val = temp