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
            
class Solution:                     #TC = O(n) and SC = O(n)
    def isValid(self, s):
        stack = stack_ll()
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.push_front(i)
            else:
                if stack.is_empty():
                    return False
                if i == ')' and stack.peek() == '(':
                    stack.pop_front()
                elif i == '}' and stack.peek() == '{':
                    stack.pop_front()
                elif i == ']' and stack.peek() == '[':
                    stack.pop_front()
                else:
                    return False
        if stack.is_empty():
            return True
        else:
            return False