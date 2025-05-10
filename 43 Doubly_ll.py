class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_ll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, data):    #O(1)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, data):    #O(1)
        if self.head is None:
            self.push_front(data)
        else:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def pop_front(self):         #O(1)
        if self.head is None:
            print('List is empty')
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            del temp
        
    def pop_back(self):          #O(1)
        if self.head is None:
            print('List is empty')
        else:
            temp = self.tail
            self.tail = temp.prev
            temp.prev = None
            del temp
    
    def insert(self, data, pos):    #O(n)
        if pos < 0:
            print('Invalid position')
        elif pos == 0:
            self.push_front(data)
        else:
            new_node = Node(data)
            temp = self.head
            for i in range(pos-1):
                if temp == None:
                    print('Invalid position')
                    return
                temp = temp.next
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
            if new_node.next is not None:
                new_node.next.prev = new_node

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end='-> ')
            temp = temp.next
        print('None')

D = Doubly_ll()
D.push_back(7)
D.push_front(5)
D.push_front(4)
D.push_front(3)
D.push_front(2)
D.push_front(1)

D.insert(6,5)

D.print_list()