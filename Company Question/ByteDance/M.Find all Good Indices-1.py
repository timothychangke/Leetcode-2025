class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        fw = [False] * len(nums)
        s = []
        for i in range(len(nums)):
            fw[i] = len(s) >= k
            if not s:
                s.append(nums[i])
            else:
                if nums[i] <= s[-1]: s.append(nums[i])
                else: s = [nums[i]]
        res = []
        s = []
        for i in range(len(nums) - 1, -1, -1):
            if len(s) >= k and fw[i]:
                res.append(i)
            if not s: s.append(nums[i])
            else:
                if nums[i] <= s[-1]: s.append(nums[i])
                else: s = [nums[i]]
        return res[::-1]