#By me
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None or list2 == None:
            return
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val <= list2.val:
            result = list1
            result.next = self.mergeTwoLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeTwoLists(list1, list2.next)
        return result
    
#By gemini
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None or list2 is None:
            if list1 is None:
                return list2
            else:
                return list1

        if list1.val <= list2.val:
            result = list1
            result.next = self.mergeTwoLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeTwoLists(list1, list2.next)

        return result