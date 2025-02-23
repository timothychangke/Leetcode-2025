# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        prev = slow.next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev, cur = cur, next
        start, end = head, prev
        while end:
            startNext, endNext = start.next, end.next
            start.next = end
            end.next = startNext
            start, end = startNext, endNext
        return head