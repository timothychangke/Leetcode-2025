# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur = head
        for _ in range(left - 1):
            cur = cur.next
        p1, p2 = cur.next, cur.next.next
        for _ in range(right - left):
            nextNode = p2.next
            p2.next = p1
            p1.next = nextNode
            cur.next = p2