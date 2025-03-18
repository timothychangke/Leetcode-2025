class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def _rob(start, end):
            h1, h2 = 0, 0
            for i in range(start, end):
                temp = max(h1 + nums[i], h2)
                h1 = h2
                h2 = temp
            return h2
        return max(_rob(0, len(nums) - 1), _rob(1, len(nums)))