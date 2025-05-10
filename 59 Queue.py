class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class queue:
    def __init__(self):
        Node.head = None
        Node.tail = None
    
    def enqueue(self,value):    #O(1)
        new_node = Node(value)
        if Node.head is None:
            Node.head = new_node
            Node.tail = new_node
        else:
            Node.tail.next = new_node
            Node.tail = new_node
    
    def dequeue(self):         #O(1)
        if Node.head is None:
            print('Queue is empty')
        else:
            temp = Node.head
            Node.head = temp.next
            temp.next = None
            del temp

    def front(self):
        if Node.head is None:
            print('Queue is empty')
        else:
            print(Node.head)

    def print_queue(self):       #O(n)
        temp = Node.head
        while temp is not None:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print('Null')

    def is_empty(self):          #O(1)
        if Node.head is None:
            return True
        else:
            return False


class doubly_queue:
    def __init__(self):
        Node.head = None
        Node.tail = None
    
    def enqueue_back(self,value):    #O(1)
        new_node = Node(value)
        if Node.head is None:
            Node.head = new_node
            Node.tail = new_node
        else:
            Node.tail.next = new_node
            Node.tail = new_node
        
    def enqueue_front(self,value):
        new_node = Node()
        if Node.head is None:
            Node.head = new_node
            Node.tail = new_node
        else:
            new_node.next = Node.head
            Node.head = new_node
    
    def dequeue_front(self):         #O(1)
        if Node.head is None:
            print('List is empty')
        else:
            temp = Node.head
            Node.head = temp.next
            temp.next = None
            del temp
        
    def dequeue_back(self):
        if Node.head is None:
            print('List is empty')
        else:
            temp = Node.head
            while temp.next is not Node.tail:
                temp = temp.next
            temp.next = None
            del Node.tail
            Node.tail = temp

    def front(self):
        if Node.head is None:
            print('Queue is empty')
        else:
            print(Node.head)

    def front(self):
        if Node.head is None:
            print('Queue is empty')
        else:
            print(Node.tail)

    def print_queue(self):       #O(n)
        temp = Node.head
        while temp is not None:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print('Null')

    def is_empty(self):          #O(1)
        if Node.head is None:
            return True
        else:
            return False