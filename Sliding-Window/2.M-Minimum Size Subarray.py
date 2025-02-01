class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, sum = 0, 0
        res = float('inf')
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                res = min(end - start + 1, res)
                sum -= nums[start]
                start += 1
        return res if res < float('inf') else 0