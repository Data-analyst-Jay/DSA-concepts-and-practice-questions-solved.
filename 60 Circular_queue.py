# Using Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class circular_queue:
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
            Node.tail.next = Node.head
    
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
        temp = Node.head.next
        print(Node.head.value , '->', end = " ")
        while temp is not Node.head:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print(Node.head.value)

    def is_empty(self):          #O(1)
        if Node.head is None:
            return True
        else:
            return False
        

# Using List

class queue_l:
    def __init__(self,cap):
        self.size = 0
        self.cap = cap
        self.l = [None] * self.cap
        self.f, self.r = 0,-1
    
    def enqueue(self,value):
        if self.size == self.cap:
            print('full')
            return 
        self.r = (self.r+1)% self.cap
        self.l[self.r] = value
        self.size += 1 

    def dequeue(self):
        if self.size == 0:
            print('Empty queue')
            return
        self.f = (self.f+1)%self.cap
        self.size -= 1
    
    def front(self):
        print(self.l[self.f])

    def print_q(self):
        if self.size == 0:
            print('Empty')
            return
        for i in range(self.size):
            print(self.l[(self.f + i) % self.cap], end=' -> ')
        print(self.l[self.f])


q = queue_l(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.print_q()