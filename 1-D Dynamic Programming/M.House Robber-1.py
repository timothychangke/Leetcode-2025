class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0, 0
        for i in range(len(nums)):
            temp = max(h1 + nums[i], h2)
            h1 = h2
            h2 = temp
        return h2
