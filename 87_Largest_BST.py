class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Info:
    def __init__(self,min,max,size):
        self.min = min
        self.max = max
        self.size = size

def helper(root):
    if root is None:
        return Info(float('inf'), float('-inf'), 0)

    left_info = helper(root.left)
    right_info = helper(root.right)

    if left_info.max < root.data < right_info.min:
        return Info(min(left_info.min, root.data), max(right_info.max, root.data), left_info.size + right_info.size + 1)
    
    return Info(float('-inf'), float('inf'), max(left_info.size, right_info.size))

def LargestBSTinBT(root):
    if root is None:
        return 0
    
    info = helper(root)
    return info.size