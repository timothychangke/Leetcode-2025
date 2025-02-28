# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevTail = ListNode()
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count += 1
            if count == k:
                prev, cur = r, l
                for _ in range(k):
                    temp = cur.next
                    cur.next = prev
                    prev, cur = cur, temp
                prevTail.next = prev
                prevTail = l
                l = r
            else:
                return dummy.next

            
        