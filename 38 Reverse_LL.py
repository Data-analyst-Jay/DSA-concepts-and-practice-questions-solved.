# TC = O(n) and SC = O(1)
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
    def print_list(self):       #O(n)
        temp = Node.head
        while temp is not None:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print('Null')

    def reverse(self):
        prev = None
        curr = Node.head
        nxt = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        Node.head = prev

ll = Linked_list()
ll.push_front(5)
ll.push_front(4)
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)
ll.print_list()
ll.reverse()
ll.print_list()