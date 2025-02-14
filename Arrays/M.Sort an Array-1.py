class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        s1 = self.sortArray(nums[:mid])
        s2 = self.sortArray(nums[mid:])
        return self.merge(s1, s2)

    def merge(self, s1, s2):
        i = j = 0
        res = []
        while i < len(s1) and j < len(s2):
            if s1[i] < s2[j]:
                res.append(s1[i])
                i += 1
            else:
                res.append(s2[j])
                j += 1
        while i < len(s1):
            res.append(s1[i])
            i += 1
        while j < len(s2):
            res.append(s2[j])
            j += 1
        return res
            

            
        