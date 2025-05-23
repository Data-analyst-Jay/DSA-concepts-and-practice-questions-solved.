class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):                          #TC = O(n)
        self.root = self._insert(self.root, val)
    
    def _insert(self, root, val):
        if root is None:
            return node(val)
        if val < root.data:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)
        return root
    
    def search(self,val):                              #TC = O(height of the BST) in balanced BST it is O(logn)
        return self._search(self.root, val)
    
    def _search(self, root, val):
        if root is None:
            return False
        if root.data == val:
            return True
        if val < root.data:
            return self._search(root.left, val)
        else:
            return self._search(root.right, val)
        
    def delete(self,val):
        self.root = self._delete(self.root, val)
    
    def getis(self,root):
        while root and root.left:
            root = root.left
        return root

    def _delete(self, root, val):
        if root is None:
            return None
        if val < root.data:
            root.left = self._delete(root.left, val)
        elif val > root.data:
            root.right = self._delete(root.right, val)
        else:
            if root.left is None and root.right is None:
                del(root)
                return None
            elif root.left is None or root.right is None:
                temp = root.left if root.left else root.right
                del(root)
                return temp
            else:
                IS = self.getis(root.right)
                root.data = IS
                self._delete(root.right, IS.data)
        
        return root
    
    def iot(self,root):
        if root == None:
            return
        self.iot(root.left)
        print(root.data)
        self.iot(root.right)


arr = [3,2,1,5,6,4]
bst = BST()
for i in arr:
    bst.insert(i)
r = bst.root
bst.iot(r)
bst.delete(3)
bst.iot(r)