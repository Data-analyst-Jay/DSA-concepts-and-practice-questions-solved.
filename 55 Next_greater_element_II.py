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
    
def nge2(arr):
    n = len(arr)
    s = stack_l()
    ans = [0 for i in range(len(arr))]
    for i in range(2*n-1, -1, -1):
        while s.is_empty() == False and s.peek() <= arr[i%n]:
            s.pop()
        if s.is_empty():
            ans[i%n] = -1
        else:
            ans[i%n] = s.peek()

        s.push(arr[i%n])
    return ans

a = [1,2,3,4,3]
print(nge2(a)) # [2,3,4,-1,4]