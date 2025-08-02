class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_bst(self, nums, st, end):
        if st > end:
            return None
        mid = st + (end-st)//2
        root = TreeNode(nums[mid])
        root.left = build_bst(nums, st, mid-1)
        root.right = build_bst(nums,mid+1, end)
        return root

def iot(self,root):
        if root == None:
            return
        self.iot(root.left)
        print(root.data)
        self.iot(root.right)

def merge(r1, r2):

    a1, a2 = [], []

    iot(r1, a1)
    iot(r2, a2)

    temp = []
    i, j = 0 , 0
    while i< len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            temp.append(a1[i])
        else:
            temp.append(a2[j])
    
    if i < len(a1): 
        temp.extend(a1[i:]) 
    else: 
        temp.extend(a2[j:])

    return build_bst(temp, 0, len(temp)-1)