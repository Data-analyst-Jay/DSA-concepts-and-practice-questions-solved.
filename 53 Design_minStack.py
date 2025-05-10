# TC = O(1) for all operations and SC = O(2n) for n elements in stack
class stack_l:
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append([value, min(value, self.list[-1][1]) if self.list else value])

    def pop(self):
        if self.is_empty():
            return None
        return self.list.pop()[0]
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[-1][0]

    def min(self):
        if self.is_empty():
            return None
        return self.list[-1][1]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
        

stack = stack_l()
stack.push(5)
stack.push(7)
stack.push(3)
stack.push(2)
# print(stack.pop())
print(stack.peek())
print(stack.min())

# TC = O(1) for all operations and SC = O(n) for n elements in stack
class stack_l:
    def __init__(self):
        self.list = []
    
    def getmin(self):
        return self.min_val
    
    def push(self, value):
        if self.is_empty():
            self.min_val = value
        if value < self.min_val:
            self.list.append(2*value - self.min_val)
            self.min_val = value
        else:
            self.list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        if self.list[-1] < self.min_val:
            self.min_val = 2*self.min_val - self.list[-1]
        return self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        if self.list[-1] < self.min_val:
            return self.min_val
        return self.list[-1]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.list)
