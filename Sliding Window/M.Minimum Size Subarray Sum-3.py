class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, sum, res = 0, 0, float('inf')
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                res = min(res, r - l + 1)
                sum -= nums[l]
                l += 1
        return res if res != float('inf') else 0
