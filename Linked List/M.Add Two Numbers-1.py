# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode()
        cur = ans
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            if sum <= 9:
                cur.next = ListNode(sum)
                carry = 0
            else:
                cur.next = ListNode(sum % 10)
                carry = 1
            cur = cur.next
            l1 = l1.next if l1.next else None
            l2 = l2.next if l2.next else None
        return ans.next
                
                
            