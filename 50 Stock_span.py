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
    
def stock_span(price):
    ans = [0]*len(price)
    stack = stack_l()
    for i in range(len(price)):
        while not stack.is_empty() and price[i] >= price[stack.peek()]:
            stack.pop()
        ans[i] = i - stack.peek() if not stack.is_empty() else i + 1
        stack.push(i)
    return ans

price = [100, 80, 60, 70, 60, 75, 85]
print(stock_span(price)) # [1, 1, 1, 2, 1, 4, 6]