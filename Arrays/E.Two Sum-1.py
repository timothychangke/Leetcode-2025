class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for idx, num in enumerate(nums):
            if target - num in map:
                return (idx, map[target - num])
            map[num] = idx