# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
        
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val > r.val:
                p.next = r
                r = r.next
            else:
                p.next = l
                l = l.next
            p = p.next
        p.next = l or r
        return dummy.next
        