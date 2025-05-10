# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        temp = head
        count = 0
        while count < 2:
            if temp == None:
                return head
            temp = temp.next
            count += 1
        prev = self.swapPairs(temp)
        temp = head
        count = 0
        while count < 2:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            count += 1
        return prev