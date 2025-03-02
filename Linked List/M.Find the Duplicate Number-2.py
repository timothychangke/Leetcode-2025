class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        cur = 0
        while True:
            cur = nums[cur]
            slow = nums[slow]
            if slow == cur: return slow