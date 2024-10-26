# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I the brute force will be two pass
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        if n == length:
            return head.next
        current = head
        for _ in range(length - n - 1):
            current = current.next
        current.next = current.next.next

        return head