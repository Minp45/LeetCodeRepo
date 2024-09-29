# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left >= right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node right before the start of the reversal
        for i in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist
        curr = prev.next
        for i in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
        
        return dummy.next
                
