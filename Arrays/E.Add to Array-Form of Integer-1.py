from collections import deque
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i, carry = len(num) - 1, 0
        q = deque()
        while i >= 0 or k > 0 or carry > 0:
            x = k % 10
            y = num[i] if i >= 0 else 0
            sum = x + y + carry
            carry = sum // 10
            sum %= 10
            q.appendleft(sum)
            i -= 1
            k //= 10
        return list(q)
            
""" 
 num = [2,1,5], k = 806
8 + 2
 sum = 1
 carry 1
 
 res = 21
 """           