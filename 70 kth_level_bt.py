class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class bt:
    def __init__(self):
        self.indx = -1
    def build_tree(self,arr):
        self.indx += 1
        if arr[self.indx] == -1:
            return None
        root = node(arr[self.indx])
        root.left = self.build_tree(arr)
        root.right = self.build_tree(arr)
        return root

def kth_level(root,k):
    if root == None:
        return
    if k == 0:
        print(root.value)
        return
    kth_level(root.left,k-1)
    kth_level(root.right,k-1)


a = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]
t = bt()
r = t.build_tree(a)
kth_level(r,2)