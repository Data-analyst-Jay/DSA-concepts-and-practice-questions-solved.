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
    
    def pot(self,root):                        #root->left_st->right_st      # TC:O(n)
        if root == None:
            return
        print(root.value)
        self.pot(root.left)
        self.pot(root.right)
    
    def iot(self,root):                        #left_st->root->right_st      # TC:O(n)
        if root == None:
            return
        self.iot(root.left)
        print(root.value)
        self.iot(root.right)

    def poot(self,root):                       #left_st->right_st->root     #TC:O(n)
        if root == None:
            return
        self.poot(root.left)
        self.poot(root.right)
        print(root.value)
    
    def lot(self,root):                       #level order traversal         #TC:O(n)
        q = []
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            print(node.value)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

    def lotl(self,root):
        q = []
        q.append(root)
        q.append(None)
        while len(q) > 0:
            node = q.pop(0)
            if node == None:
                if len(q) > 0:
                    print(end=' ')
                    q.append(None)
                    continue
                else:
                    break
            print(node.value)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
            
    def height(self,root):                      #TC = O(n)
        if root == None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh,rh) +1
    
    def count_nodes(self,root):                  #TC = O(n)
        if root == None:
            return 0
        return self.count_nodes(root.left) + self.count_nodes(root.right) + 1
    
    def sum_nodes(self,root):                  #TC = O(n)
        if root == None:
            return 0
        return self.sum_nodes(root.left) + self.sum_nodes(root.right) + root.value
    
def is_identical(p,q):
    if p==None and q==None:
        return True
    if p==None or q==None:
        return False
    if p.value!=q.value:
        return False
    is_left = is_identical(p.left,q.left)
    is_right = is_identical(p.right,q.right)
    return p.value==q.value and is_left and is_right