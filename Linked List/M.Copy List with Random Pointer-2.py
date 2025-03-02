"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}
        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val, cur.next, cur.random)
            cur = cur.next
        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[copy.next]
            copy.random = oldToNew[copy.random]
            cur = cur.next
        return oldToNew[head]