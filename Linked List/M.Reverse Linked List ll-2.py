# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = dummy = ListNode()
        dummy.next = head
        for _ in range(left - 1):
            cur = cur.next
        start, end = cur, cur.next
        for _ in range(right - left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp
        return dummy.next