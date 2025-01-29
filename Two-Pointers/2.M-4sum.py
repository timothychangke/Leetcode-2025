class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, arr = [], []
        def ksum(k, target, start):
            if k > 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]: continue
                    arr.append(nums[i])
                    ksum(k - 1, target - nums[i], i + 1)
                    arr.pop()
                return 
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(arr + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        ksum(4, target, 0)
        return res
        
                