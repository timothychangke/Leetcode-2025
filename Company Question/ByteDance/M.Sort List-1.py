# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        left_half = head
        temp = self.mid(head)
        right_half = temp.next
        temp.next = None
        left = self.sortList(left_half)
        right = self.sortList(right_half)
        return self.merge(left, right)
    
    def merge(self, a, b):
        l = dummyNode = ListNode()
        while a and b:
            if a.val > b.val:
                l.next = ListNode(b.val)
                b = b.next
            else:
                l.next = ListNode(a.val)
                a = a.next
            l = l.next
        if a:
            l.next = a
        elif b:
            l.next = b
        return dummyNode.next
    
    def mid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
         
        