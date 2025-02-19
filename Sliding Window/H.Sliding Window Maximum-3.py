from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        q = deque()
        for r in range(len(nums)):
            while q and nums[r] >= nums[q[-1]]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()   
            if r - l + 1 == k:
                l += 1
                res.append(nums[q[0]])
        return res
    
"""  
Input: nums = [1,3,-1,-3,-15,3,6,7], k = 3 
q = [1 2 3]
res = []
l = 1

"""