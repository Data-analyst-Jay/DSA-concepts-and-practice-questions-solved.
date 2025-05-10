# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        temp = head
        count = 0
        while count < k:
            if temp == None:
                return head
            temp = temp.next
            count += 1
        prev = self.reverseKGroup(temp, k)
        temp = head
        count = 0
        while count < k:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
            count += 1
        return prev