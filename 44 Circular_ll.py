class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class circular_ll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self,value):    #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
    
    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while temp != self.tail:
                print(temp.value,end="->")
                temp = temp.next
            print(temp.value,end="->")
            print(self.head.value)

    def insert_tail(self,value):    #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        
    def delete_head(self):    #O(1)
        if self.head is None:
            print("Linked list is empty")
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else:
            temp = self.head
            self.head = self.head.next
            self.tail.next = self.head
            temp.next = None
            del temp

    def delete_tail(self):    #O(n)
        if self.head is None:
            print("Linked list is empty")
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            del temp
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail.next = None
            del self.tail
            self.tail = temp

dll = circular_ll()
dll.insert_head(10)
dll.insert_head(20)
dll.insert_head(30)
dll.insert_head(40)
dll.insert_head(50)
dll.print_ll()