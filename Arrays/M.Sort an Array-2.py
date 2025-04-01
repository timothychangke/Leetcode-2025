class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        s1 = self.sortArray(nums[:mid])
        s2 = self.sortArray(nums[mid + 1:])
        return self.merge(s1, s2)

    def merge(s1, s2):
        i = j = 0
        res = []
        while i < len(s1) and j < len(s2):
            if s1[i] < s2[j]:
                res.append(s1[i])
                i += 1
            else:
                res.append(s2[j])
                j += 1
        if i < len(s1):
            res += s1[i:]
        if j < len(s2):
            res += s2[j:]
        return res


""" 
break array up into small sections, then merge them back together
sortArray will be recursive break until len = 1
merge them back 

5 1 1 2 2 0
5 1 1   2 2 0
5  11   2  2 0
5  1  1  2  2  0
5   11     2   02
115     022
011225
"""
