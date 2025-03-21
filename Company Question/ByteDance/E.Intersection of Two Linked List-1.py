# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        lenA, lenB = 0, 0
        while a:
            a = a.next
            lenA += 1
        while b:
            b = b.next
            lenB += 1
        if lenA < lenB: a, b = headB, headA
        else: a, b = headA, headB
        for i in range(abs(lenA - lenB)):
            a = a.next
        while a and b:
            if a is b:
                return a
            a = a.next
            b = b.next
        return None