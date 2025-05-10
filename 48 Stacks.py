# Stacks using lists
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

# Stacks using linked lists

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class stack_ll:
    def __init__(self):
        Node.head = None
        Node.tail = None
    
    def push_front(self,value):    #O(1)
        new_node = Node(value)
        if Node.head is None:
            Node.head = new_node
            Node.tail = new_node
        else:
            new_node.next = Node.head
            Node.head = new_node
    
    def pop_front(self):         #O(1)
        if Node.head is None:
            print('Stack is empty')
        else:
            temp = Node.head
            Node.head = temp.next
            temp.next = None
            del temp
    
    def peek(self):             #O(1)
        if Node.head is None:
            return None
        else:
            return Node.head.value
        
    def is_empty(self):         #O(1)
        if Node.head is None:
            return True
        else:
            return False
    
    def print_stack(self):       #O(n)
        temp = Node.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

s = stack_ll()
s.push_front(1)
s.push_front(2)
s.push_front(3)
s.print_stack()
print(s.peek())
s.pop_front()
s.print_stack()