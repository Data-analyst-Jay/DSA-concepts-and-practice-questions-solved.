class stack_l:
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[-1]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.list)
    
def pse(arr):
    s = stack_l()
    ans = []
    for i in range(len(arr)):
        while s.is_empty()==False and s.peek() >= arr[i]:
            s.pop()
        if s.is_empty():
            ans.append(-1)
        else:
            ans.append(s.peek())
        s.push(arr[i])
    return ans

a = [3,1,0,8,6]
print(pse(a)) # [-1, -1, -1, 0, 0]
# Time complexity: O(2n)
# Space complexity: O(n)