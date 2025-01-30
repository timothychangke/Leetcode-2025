class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, tot = 0, 0
        res = float('inf')
        for i in range(len(nums)):
            tot += nums[i]
            while tot >= target:
                res = min(res, i - s + 1)
                tot -= nums[s]
                s += 1
                if tot == target:
                    res = min(res, i - s + 1)
            print(tot)
        return res if res != float('inf') else 0