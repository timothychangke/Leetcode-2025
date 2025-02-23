
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        cur = 0
        while True:
            cur = nums[cur]
            slow = nums[slow]
            if slow == cur:
                return cur
        

""" 
Floyds algorithm:
with a slow and a fast pointer, the difference between them increments by one every jump
when this difference becomes a multiple of the cycles length, they wouldve met
from the point they meet, the distance from this point to the start of the cycle (+ some multiple of full laps) is the distance from the head to the cycle
"""