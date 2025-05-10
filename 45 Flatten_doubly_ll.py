"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head):
        if head == None:
            return None
        curr = head
        while curr:
            if curr.child:
                next = curr.next
                curr.next = self.flatten(curr.child)
                curr.next.prev = curr
                curr.child = None
                while curr.next:
                    curr = curr.next
                if next:
                    curr.next = next
                    next.prev = curr
            curr = curr.next
        return head