# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if not lists:
            return None

        midpoint = len(lists) // 2
        left = self.mergeKLists(lists[:midpoint])
        right = self.mergeKLists(lists[midpoint:])
        
        dummy = ListNode(-1)
        current = dummy
        while left and right:
            if left.val <= right.val:
                current.next = left
                current = left
                left = left.next
            else:
                current.next = right
                current = right
                right = right.next
        current.next = left if left else right
        return dummy.next