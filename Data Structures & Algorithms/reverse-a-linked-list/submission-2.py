# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        self.tail = head
        previous = None
        current = self.tail
        while current:
            forward = current.next
            current.next = previous
            previous = current
            current = forward

        
        return previous
        