class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list:
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
    
    def push_back(self,value):    #O(1)
        if Node.head is None:
            self.push_front(value)
        else:
            new_node = Node(value)
            Node.tail.next = new_node
            Node.tail = new_node
    
    def pop_front(self):         #O(1)
        if Node.head is None:
            print('List is empty')
        else:
            temp = Node.head
            Node.head = temp.next
            temp.next = None
            del temp

    def pop_back(self):          #O(n)
        if Node.head is None:
            print('List is empty')
        else:
            temp = Node.head
            while temp.next is not Node.tail:
                temp = temp.next
            temp.next = None
            del Node.tail
            Node.tail = temp
    
    def insert(self,value,pos):    #O(n)
        if pos < 0:
            print('Invalid position')
        elif pos == 0:
            self.push_front(value)
        else:
            new_node = Node(value)
            temp = Node.head
            for i in range(pos-1):
                if temp == 'Null':
                    print('Invalid position')
                    return
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

    def search(self,key):       #O(n)
        indx = 0
        temp = Node.head
        while temp is not None:
            if temp.value == key:
                print(indx)
            temp = temp.next
            indx+=1
        return -1
    
    def print_list(self):       #O(n)
        temp = Node.head
        while temp is not None:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print('Null')


L = Linked_list()
L.push_front(10)
L.push_front(20)
L.push_front(30)
L.push_back(0)
L.pop_front()
L.pop_back()
L.insert(30,1)
L.search(30)

L.print_list()