# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # null checker
        if not head:
            return None
        # create a slow and fast pointer
        slow = fast = head
        # interate the slow and fast until they meet
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # ensure the the cycle exist
        if fast is None or fast.next is None:
            return None 
        # interate fast and head again to see where they meet
        temp = head
        while temp != fast:
            temp = temp.next
            fast = fast.next
        
        return temp