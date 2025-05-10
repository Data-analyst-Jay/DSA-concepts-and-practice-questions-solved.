class queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self,value):    #O(1)
        self.q.append(value)
    
    def dequeue(self):         #O(1)
        if len(self.q) == 0:
            print('Queue is empty')
        else:
            return(self.q.pop(0))

    def front(self):
        if self.is_empty():
            print('Queue is empty')
        else:
            return(self.q[0])

    def print_queue(self):       #O(n)
        if len(self.q) == 0:
            print('Empty')
            return
        for i in self.q:
            print(i, end=' ')

    def is_empty(self):          #O(1)
        if len(self.q) == 0:
            return True
        else:
            return False
        

class stack:
    def __init__(self):
        self.p = queue()
        self.h = queue()
    
    def push(self,value):                     #O(n)
        while not self.p.is_empty():
            self.h.enqueue(self.p.front())
            self.p.dequeue()
        self.p.enqueue(value)
        while not self.h.is_empty():
            self.p.enqueue(self.h.front())
            self.h.dequeue()
    
    def pop(self):                           #O(1)
        if self.p.front() is None:
            print('Stack is empty')
        else:
            print(self.p.dequeue())
    
    def top(self):
        if self.p.is_empty():
            print('stack is empty')
        else:
            print(self.p.front())
        
    def is_empty(self):                     #O(1)
        if self.p.is_empty():
            return True
        else:
            return False
        
    def s_print(self):
        self.p.print_queue()
    
s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

s.s_print()

s.pop()

s.s_print()


# Queues Using Stacks 
class stack:
    def __init__(self):
        self.list = []
    
    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.list[0]
    
    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False
        
class queue:
    def __init__(self):
        self.p = stack()
        self.h = stack()

    def enqueue(self,value):
        while not self.p.is_empty:
            self.h.push(self.p.peek())
            self.p.pop()
        self.p.push(value)
        while not self.h.is_empty():
            self.p.push(self.h.peek())
            self.h.pop()

    def dequeue(self):
        if self.p.peek() is None:
            print('Queue is empty')
        else:
            print(self.p.pop())

    def front(self):
        if self.p.is_empty():
            print('Queue is empty')
        else:
            print(self.p.peek())
        
    def is_empty(self):                     #O(1)
        if self.p.is_empty():
            return True
        else:
            return False