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

def subtree(r,sr):
    if r==None or sr==None:
        return r==sr
    if r.value == sr.value and is_identical(r,sr):
        return True
    return subtree(r.left,sr) or subtree(r.right,sr)