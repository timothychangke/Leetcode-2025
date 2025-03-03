# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        for _ in range(n): p2 = p2.next
        if not p2: return head.next
        while p2.next:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head
        