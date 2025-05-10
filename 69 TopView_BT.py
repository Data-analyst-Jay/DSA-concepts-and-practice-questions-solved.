def topview(self,root):                    #TC :O(n) SC:O(n)
        if root == None:
            return
        q = []        #(node,hd)
        map = {}      #(hd, node.value)
        q.append({root,0})
        while len(q) > 0:
            node = q.pop([0][0])
            hd = q.pop([0][1])
            if hd not in map:
                map[hd] = node.value
            print(node.value)

            if node.left != None:
                q.append({node.left,hd-1})
            if node.right != None:
                q.append({node.right,hd+1})
        for i in sorted(map.keys()):
            print(map[i],end=' ')