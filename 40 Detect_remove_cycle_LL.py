# TC = O(n) and SC = O(1)
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self,value):    #O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self):       #O(n)
        temp = self.head
        while temp is not None:
            print(temp.value , '->', end = " ")
            temp = temp.next
        print('Null')

    def det_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
                break
        return slow, fast
        return False
    
    def remove_cycle(self):
        if self.det_cycle() == True:
            slow = self.head
            fast = self.det_cycle()
            prev = None
            while slow != fast:
                slow = slow.next
                prev = fast
                fast = fast.next
            prev.next = None
            return slow.value

ll = Linked_list()
ll.push_front(6)
ll.push_front(5)
ll.push_front(4)
ll.push_front(3)
ll.push_front(2)
ll.push_front(1)
ll.print_list()