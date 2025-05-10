# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        m = {}
        old_node = head
        new_node = Node(old_node.val)
        m[old_node] = new_node
        old_temp = old_node.next
        new_temp = new_node
        while old_temp:
            new_temp.next = Node(old_temp.val)
            new_temp = new_temp.next
            m[old_temp] = new_temp
            old_temp = old_temp.next
        
        old_temp = old_node
        new_temp = new_node
        while old_temp:
            if old_temp.random:
                new_temp.random = m[old_temp.random]
            old_temp = old_temp.next
            new_temp = new_temp.next
        
        return new_node